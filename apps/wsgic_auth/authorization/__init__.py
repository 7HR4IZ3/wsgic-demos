from wsgic.helpers import hooks
from wsgic.services import service
from wsgic_auth.models import UsersPermissions
# from wsgic.utils.php_py import *
from .models import GroupModel, PermissionModel

is_array = lambda x: isinstance(x, list)
is_numeric = lambda x: isinstance(x, int)
is_string = lambda x: isinstance(x, str)
in_array = lambda key, arr, e: key in arr
array_column = lambda arr, key: [x.get(key) for x in arr] 
lang = lambda *x: "Lang..."
strtolower = lambda x: x.lower()
count = len


class Authorization:
    """
     * @var array|string|None
    """
    error = None

    """
     * The group model to use. Usually the class noted
     * below (or an extension thereof) but can be any
     * compatible CodeIgniter Model.
     *
     * @var GroupModel
    """
    group_model = None

    """
     * The group model to use. Usually the class noted
     * below (or an extension thereof) but can be any
     * compatible CodeIgniter Model.
     *
     * @var PermissionModel
    """
    permission_model = None

    """
     * The group model to use. Usually the class noted
     * below (or an extension thereof) but can be any
     * compatible CodeIgniter Model.
     *
     * @var UserModel
    """
    user_model = None

    """
     * Stores the models.
     *
     * @param GroupModel      groupModel
     * @param PermissionModel permissionModel
     *
     * @return array|string|None
    """
    def __init__(self, groupModel=GroupModel, permissionModel=PermissionModel):
        self.group_model: GroupModel = groupModel()
        self.permission_model: PermissionModel = permissionModel()


    """
     * Allows the consuming application to pass in a reference to the
     * model that should be used.
     *
     * @param UserModel model
     *
     * @return mixed
    """
    def set_user_model(self, model):
        self.user_model = model

        return self


    #____________________________________________________________________
    # Actions
    #____________________________________________________________________

    """
     * Checks to see if a user is in a group.
     *
     * Groups can be either a string, with the name of the group, an INT
     * with the ID of the group, or an array of strings/ids that the
     * user must belong to ONE of. (It's an OR check not an AND check)
     *
     * @param mixed groups
     *
     * @return not 
    """
    def in_group(self, groups, userId):
        if (userId == 0):
            return False
    

        if (not is_array(groups)):
            groups = [groups]

        userGroups = self.group_model.get_groups_for_user(int(userId))
        # print(groups, userGroups)

        if not userGroups:
            return False

        for group in groups:
            if (is_numeric(group)):
                ids = [x.group.id for x in userGroups]
                if group in ids:
                    return True
            
            elif (is_string(group)):
                    names = [x.group.name for x in userGroups]

                    if group in names:
                        return True
        return False


    """
     * Checks a user's groups to see if they have the specified permission.
     *
     * @param int|string permission Permission ID or name
     *
     * @return mixed
    """
    def has_permission(self, permission, userId):
        # @phpstan_ignore_next_line
        if (not (permission) or (not is_string(permission) and not is_numeric(permission))):
            return None
    

        if (not (userId) or not is_numeric(userId)):
            return None
    

        # Get the Permission ID
        permissionId = self.get_permission_id(permission)

        if (not is_numeric(permissionId)):
            return False
    

        # First check the permission model. If that exists, then we're golden.
        if (self.permission_model.does_user_have_permission(userId, permissionId)):
            return True
    

        # Still here? Then we have one last check to make _ any user private permissions.
        return self.does_user_have_permission(userId, permissionId)


    """
     * Makes a member a part of a group.
     *
     * @param mixed group Either ID or name, fails on anything else
     *
     * @return not |None
    """
    def add_user_to_group(self, userid, group):
        if (not (userid) or not is_numeric(userid)):
            return None

        if (not (group) or (not is_numeric(group) and not is_string(group))):
            return None
    

        groupId = self.get_group_id(group)

        if (not hooks.trigger('before_add_user_to_group', userid, groupId)):
            return False
    

        # Group ID
        if (not is_numeric(groupId)):
            return None
    

        if (not self.group_model.add_user_to_group(userid, groupId)):
            # self.error = self.group_model.errors()

            return False
    

        hooks.trigger('add_user_to_group', userid, groupId)

        return True


    """
     * Removes a single user from a group.
     *
     * @param mixed group
     *
     * @return mixed
    """
    def remove_user_from_group(self, userId, group):
        if (not (userId) or not is_numeric(userId)):
            return None
    

        if (not (group) or (not is_numeric(group) and not is_string(group))):
            return None
    

        groupId = self.get_group_id(group)

        if (not hooks.trigger('before_remove_user_from_group', userId, groupId)):
            return False
    

        # Group ID
        if (not is_numeric(groupId)):
            return False
    

        if (not self.group_model.remove_user_from_group(userId, groupId)):
            # self.error = self.group_model.errors()

            return False
    

        hooks.trigger('remove_user_from_group', userId, groupId)

        return True


    """
     * Adds a single permission to a single group.
     *
     * @param int|string permission
     * @param int|string group
     *
     * @return mixed
    """
    def add_permission_to_group(self, permission, group):
        permissionId = self.get_permission_id(permission)
        groupId      = self.get_group_id(group)

        # Permission ID
        if (not is_numeric(permissionId)):
            return False
    

        # Group ID
        if (not is_numeric(groupId)):
            return False
    

        # Remove itnot
        if (not self.group_model.add_permission_to_group(permissionId, groupId)):
            # self.error = self.group_model.errors()

            return False
    

        return True


    """
     * Removes a single permission from a group.
     *
     * @param int|string permission
     * @param int|string group
     *
     * @return mixed
    """
    def remove_permission_from_group(self, permission, group):
        permissionId = self.get_permission_id(permission)
        groupId      = self.get_group_id(group)

        # Permission ID
        if (not is_numeric(permissionId)):
            return False
    

        # Group ID
        if (not is_numeric(groupId)):
            return False
    

        # Remove itnot
        if (not self.group_model.remove_permission_from_group(permissionId, groupId)):
            # self.error = self.group_model.errors()

            return False
    

        return True


    """
     * Assigns a single permission to a user, irregardless of permissions
     * assigned by roles. self is saved to the user's meta information.
     *
     * @param int|string permission
     *
     * @return not |None
    """
    def add_permission_to_user(self, permission, userId):
        permissionId = self.get_permission_id(permission)

        if (not is_numeric(permissionId)):
            return None
    

        if (not hooks.trigger('before_add_permission_to_user', userId, permissionId)):
            return False
    

        user = self.user_model.model.Meta.objects.get(id=userId)

        if (not user):
            self.error = lang('Auth.userNotFound', [userId])

            return False
    

        """ @var User user"""
        permissions = UsersPermissions.Meta.objects.get(user=userId)

        if (not in_array(permissionId, permissions, True)):
            self.permission_model.add_permission_to_user(permissionId, user.id)
    

        hooks.trigger('add_permission_to_user', userId, permissionId)

        return True


    """
     * Removes a single permission from a user. Only applies to permissions
     * that have been assigned with addPermissionToUser, not to permissions
     * inherited based on groups they belong to.
     *
     * @param int|string permission
     *
     * @return not |mixed|None
    """
    def remove_permission_from_user(self, permission, userId):
        permissionId = self.get_permission_id(permission)

        if (not is_numeric(permissionId)):
            return False
    

        if (not (userId) or not is_numeric(userId)):
            return None
    

        userId = int(userId)

        if (not hooks.trigger('before_remove_permission_from_user', userId, permissionId)):
            return False
    

        return self.permission_model.remove_permission_from_user(permissionId, userId)


    """
     * Checks to see if a user has private permission assigned to it.
     *
     * @param int|string userId
     * @param int|string permission
     *
     * @return not |None
    """
    def does_user_have_permission(self, userId, permission):
        permissionId = self.get_permission_id(permission)

        if (not is_numeric(permissionId)):
            return False
    

        if (not (userId) or not is_numeric(userId)):
            return None
    

        return self.permission_model.does_user_have_permission(userId, permissionId)


    #____________________________________________________________________
    # Groups
    #____________________________________________________________________

    """
     * Grabs the details about a single group.
     *
     * @param int|string group
     *
     * @return object|None
    """
    def group(self, group):
        if (is_numeric(group)):
            return self.group_model.find(int(group))
    

        return self.group_model.model.Meta.objects.get(name=group).first()


    """
     * Grabs an array of all groups.
     *
     * @return array of objects
    """
    def groups(self):
        return self.group_model.model.Meta.objects.get()


    """
     * @return mixed
    """
    def create_group(self, name, description = None):
        gid = self.get_group_id(name)
        if gid:
            return gid
        
        data = {
            'name'        : name,
            'description' : description or "",
        }

        validation = service('validation')

        validation.set_rules({
            'name'        : 'required|max_length(255)',
            'description' : 'max_length(255)',
        })

        if (not validation.validate(data)):
            self.error = validation.errors()

            return False

        # print(self.group_model.model.Meta.database, self.group_model.model.Meta.database.models)
        self.group_model.model.Meta.objects.create(**data)
        id = self.group_model.model.Meta.objects.get_one(**data).id


        if (is_numeric(id)):
            return int(id)
        # self.error = self.group_model.errors()

        return False


    """
     * Deletes a single group.
     *
     * @return not 
    """
    def delete_group(self, groupId):
        if (not self.group_model.model.Meta.objects.delete(**{"id": groupId})):
            # self.error = self.group_model.errors()
            return False
        return True


    """
     * Updates a single group's information.
     *
     * @return mixed
    """
    def update_group(self, id, name, description = ''):
        data = {}
        if name:
            data["name"] = name

        if (not not (description)):
            data['description'] = description
    

        if (not self.group_model.model.Meta.objects.update(data, id=id)):
            # self.error = self.group_model.errors()

            return False
    

        return True


    """
     * Given a group, will return the group ID. The group can be either
     * the ID or the name of the group.
     *
     * @param int|string group
     *
     * @return False|int
    """
    def get_group_id(self, group):
        if (is_numeric(group)):
            return int(group)

        g = self.group_model.model.Meta.objects.get(name=group)

        if (not g):
            self.error = lang('Auth.groupNotFound', [group])
            return False

        return int(g.first().id)


    #____________________________________________________________________
    # Permissions
    #____________________________________________________________________

    """
     * Returns the details about a single permission.
     *
     * @param int|string permission
     *
     * @return object|None
    """
    def permission(self, permission):
        if (is_numeric(permission)):
            return self.permission_model.model.Meta.objects.get(id=int(permission))

        return self.permission_model.model.Meta.objects.get(name=permission).first()


    """
     * Returns an array of all permissions in the system.
     *
     * @return mixed
    """
    def permissions(self):
        return self.permission_model.model.Meta.objects.get()


    """
     * Creates a single permission.
     *
     * @return mixed
    """
    def create_permission(self, name, description = ''):
        data = {
            'name'        : name,
            'description' : description,
        }

        validation = service('validation', None, False)
        validation.setRules({
            'name'        : 'required|max_length(255)',
            'description' : 'max_length(255)',
        })

        if (not validation.validate(data)):
            self.error = validation.errors()

            return False
    

        self.permission_model.model.Meta.objects.create(**data)
        id = self.permission_model.model.Meta.objects.get_one(**data).id

        if (is_numeric(id)):
            return int(id)
    

        # self.error = self.permission_model.errors()

        return False


    """
     * Deletes a single permission and removes that permission from all groups.
     *
     * @return mixed
    """
    def delete_permission(self, permissionId):
        if (not self.permission_model.model.Meta.objects.delete(id=permissionId)):
            # self.error = self.permission_model.errors()

            return False
    

        # Remove the permission from all groups
        self.group_model.remove_permission_from_all_groups(permissionId)

        return True


    """
     * Updates the details for a single permission.
     *
     * @return not 
    """
    def update_permission(self, id, name, description = ''):
        data = {
            'name' : name,
        }

        if (not not (description)):
            data['description'] = description
    

        if (not self.permission_model.model.Meta.objects.update(data, id=id)):
            # self.error = self.permission_model.errors()

            return False
    

        return True


    """
     * Verifies that a permission (either ID or the name) exists and returns
     * the permission ID.
     *
     * @param int|string permission
     *
     * @return False|int
    """
    def get_permission_id(self, permission):
        # If it's a number, we're done here.
        if (is_numeric(permission)):
            return int(permission)
    

        # Otherwise, pull it from the database.
        p = self.permission_model.model.Meta.objects.get(name=permission).first()

        if (not p):
            self.error = lang('Auth.permissionNotFound', [permission])

            return False
    

        return int(p.id)


    """
     * Returns an array of all permissions in the system for a group
     * The group can be either the ID or the name of the group.
     *
     * @param int|string group
     *
     * @return mixed
    """
    def group_permissions(self, group):
        if (is_numeric(group)):
            return self.group_model.get_permissions_for_group(group)
    

        g = self.group_model.model.Meta.objects.get(name=group).first()

        return self.group_model.get_permissions_for_group(g.id)


    """
     * Returns an array of all users in a group
     * The group can be either the ID or the name of the group.
     *
     * @param int|string group
     *
     * @return mixed
    """
    def users_in_group(self, group):
        if (is_numeric(group)):
            return self.group_model.get_users_for_group(group)
    

        g = self.group_model.model.Meta.objects.get(name=group).first()

        return self.group_model.get_users_for_group(g.id)
