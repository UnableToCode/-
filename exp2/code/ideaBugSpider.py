import json

import requests


def ideaBugSpider():
    _urlID = 'https://youtrack.jetbrains.com/api/sortedIssues?$top=-1&fields=tree(id,matches,ordered,parentId,' \
             'summaryTextSearchResult(highlightRanges(endOffset,startOffset),textRange(endOffset,startOffset)))' \
             '&flatten=true&folderId=22-22&query=Type:+Bug&skipRoot={page}00&topRoot=101'

    _urlIssue = 'https://youtrack.jetbrains.com/api/issuesGetter?$top=-1&fields=$type,attachments(id),' \
                'commentsCount,created,fields(projectCustomField(field(name)),value(color(id),localizedName,name)),' \
                'fields($type,hasStateMachine,id,name,projectCustomField($type,bundle(id),canBeEmpty,emptyFieldText,' \
                'field(fieldType(isMultiValue,valueType),id,localizedName,name,ordinal),id,isPublic,ordinal,size),' \
                'value($type,archived,avatarUrl,buildLink,color(id),fullName,id,isResolved,localizedName,login,' \
                'markdownText,minutes,name,presentation,ringId,text)),id,idReadable,project($type,id,name,ringId,' \
                'shortName),reporter($type,avatarUrl,email,fullName,id,isLocked,issueRelatedGroup(icon),login,name,' \
                'online,ringId),reporter($type,fullName,id,isLocked),resolved,summary,tags(color(id),id,name,' \
                'owner(id),query),transaction(timestamp,authorId),updated,updated,updater($type,avatarUrl,email,' \
                'fullName,id,isLocked,issueRelatedGroup(icon),login,name,online,ringId),visibility($type,' \
                'implicitPermittedUsers($type,avatarUrl,email,fullName,id,isLocked,issueRelatedGroup(icon),login,' \
                'name,online,ringId),permittedGroups($type,allUsersGroup,icon,id,name,ringId),permittedUsers' \
                '($type,avatarUrl,email,fullName,id,isLocked,issueRelatedGroup(icon),login,name,online,ringId)),' \
                'voters(hasVote),votes,watchers(hasStar)'

    urlsID = [_urlID.format(page=page) for page in range(0, 1210)]

    payloadHeader = {
        'Content-Type': 'application/json',
    }

    result = list()

    cnt = 0
    for urlID in urlsID:
        cnt += 1
        id = list()
        resID = requests.get(urlID)
        resID.encoding = 'utf-8'
        json_resID = json.loads(resID.text)

        for one in json_resID['tree']:
            id.append({'id': one['id']})
        # print(id)

        payloadData = id

        resIssue = requests.post(url=_urlIssue, data=json.dumps(payloadData), headers=payloadHeader)
        resIssue.encoding = 'utf-8'
        json_resIssue = json.loads(resIssue.text)

        # print(json_resIssue)

        for one in json_resIssue:
            subSystem = str()
            if one['fields'][4]['value'] is None:
                subSystem = None
            else:
                subSystem = one['fields'][4]['value']['name']

            result.append({'summary': one['summary'],
                           'priority': one['fields'][0]['value']['name'],
                           'state': one['fields'][2]['value']['name'],
                           'subSystem': subSystem})

        print(cnt)

    with open("result.json", 'w+') as f:
        json.dump(result, f)


if __name__ == '__main__':
    ideaBugSpider()
