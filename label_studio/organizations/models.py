"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
import logging

from django.db import models, transaction
from django.conf import settings
from django.db.models import Q, Count
from django.contrib.auth.models import Group

from django.utils.translation import gettext_lazy as _

from core.utils.common import create_hash, get_organization_from_request, load_func

logger = logging.getLogger(__name__)


class InvitedPeople(models.Model):

    email = models.CharField(_('email'), max_length=1000, null=False)
    
    role = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='role',
        help_text='Role'
    )

    organization = models.ForeignKey(
        'organizations.Organization', on_delete=models.CASCADE,
        help_text='Organization ID'
    )

    invited_at = models.DateTimeField(_('invited at'), auto_now_add=True)

    def created_at_prettify(self):
        return self.invited_at.strftime("%d %b %Y %H:%M:%S")

    class Meta:
        db_table = 'invited_people'


class OrganizationMember(models.Model):
    """
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='om_through',
        help_text='User ID'
    )
    organization = models.ForeignKey(
        'organizations.Organization', on_delete=models.CASCADE,
        help_text='Organization ID'
    )

    role = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='member_role',
        help_text='Role', to_field='id', default=4
    )
    
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    @classmethod
    def find_by_user(cls, user_or_user_pk, organization_pk):
        from users.models import User

        user_pk = user_or_user_pk.pk if isinstance(user_or_user_pk, User) else user_or_user_pk
        return OrganizationMember.objects.get(user=user_pk, organization=organization_pk)

    @property
    def is_owner(self):
        return self.user.id == self.organization.created_by.id

    class Meta:
        ordering = ['pk']


OrganizationMixin = load_func(settings.ORGANIZATION_MIXIN)


class Organization(OrganizationMixin, models.Model):
    """
    """
    title = models.CharField(_('organization title'), max_length=1000, null=False)

    token = models.CharField(_('token'), max_length=256, default=create_hash, unique=True, null=True, blank=True)

    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="organizations", through=OrganizationMember)

        
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                      null=True, related_name="organization", verbose_name=_('created_by'))

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.title + ', id=' + str(self.pk)

    @classmethod
    def create_organization(cls, created_by=None, title='Your Organization'):
        _create_organization = load_func(settings.CREATE_ORGANIZATION)
        return _create_organization(title=title, created_by=created_by)
    
    @classmethod
    def find_by_user(cls, user):
        memberships = OrganizationMember.objects.filter(user=user).prefetch_related('organization')
        if not memberships.exists():
            raise ValueError(f'No memberships found for user {user}')
        return memberships.first().organization

    @classmethod
    def find_by_invite_url(cls, url):
        token = url.strip('/').split('/')[-1]
        if len(token):
            return Organization.objects.get(token=token)
        else:
            raise KeyError(f'Can\'t find Organization by welcome URL: {url}')

    def has_user(self, user):
        return self.users.filter(pk=user.pk).exists()

    def has_project_member(self, user):
        return self.projects.filter(members__user=user).exists()

    def has_permission(self, user):
        if self in user.organizations.all():
            return True
        return False

# TODO: Thêm role chỗ này
    def add_user(self, user):
        if self.users.filter(pk=user.pk).exists():
            logger.debug('User already exists in organization.')
            return
        member= InvitedPeople.objects.get(email=user.email)
        with transaction.atomic():
            # Thêm vào tổ chức
            om = OrganizationMember(user=user, organization=self, role=member.role)
            om.save()
            # Xóa khỏi danh sách người được mời
            member.delete()
            # Thêm vào nhóm quyền
            membergroup= Group.objects.get(id=member.role_id)
            membergroup.user_set.add(user)
            
            return om    
    
    def reset_token(self):
        self.token = create_hash()
        self.save()

    def check_max_projects(self):
        """This check raise an exception if the projects limit is hit
        """
        pass

    def invitedToOrg(self, email, role):
        member = InvitedPeople(email=email, role_id=role, organization=self)
        member.save()
        return member
        
    def projects_sorted_by_created_at(self):
        return self.projects.all().order_by('-created_at').annotate(
            tasks_count=Count('tasks'),
            labeled_tasks_count=Count('tasks', filter=Q(tasks__is_labeled=True))
        ).prefetch_related('created_by')

    def created_at_prettify(self):
        return self.created_at.strftime("%d %b %Y %H:%M:%S")

    def per_project_invited_users(self):
        from users.models import User
        invited_ids = self.projects.values_list('members__user__pk', flat=True).distinct()
        per_project_invited_users = User.objects.filter(pk__in=invited_ids)
        return per_project_invited_users

    @property
    def secure_mode(self):
        return False

    @property
    def members(self):
        return OrganizationMember.objects.filter(organization=self)

    @property
    def invited(self):
        return InvitedPeople.objects.filter(organization=self)

    class Meta:
        db_table = 'organization'