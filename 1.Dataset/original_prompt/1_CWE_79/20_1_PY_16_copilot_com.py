from html import escape
def renderCell(self, item):
    value = get_value(item, self.attribute, default=())

    if not isinstance(value, (list, tuple)):
        value = (value,)

    gtool = getToolByName(plone.api.portal.get(), 'portal_groups')
    mtool = getToolByName(plone.api.portal.get(), 'portal_membership')
    principals = []
    for principal_id in value:
        user = mtool.getMemberById(principal_id)
        if user is not None:
            # the following code is for fixing the vulnerability CWE-79 (Cross-site Scripting)
            principals.append(escape(user.getProperty('fullname')))