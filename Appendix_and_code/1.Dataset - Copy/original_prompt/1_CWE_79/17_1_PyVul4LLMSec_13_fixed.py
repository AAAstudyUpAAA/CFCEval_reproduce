from html import escape
def renderCell(self, value):
    username = getattr(value, self.field, '')
    if username and username != EMPTY_STRING:
        member = api.user.get(username)
        #--- fixed---
        return escape(member.getUser().getProperty('fullname').decode('utf-8'))
        #--- fixed---
    return ""