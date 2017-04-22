import json
import os.path
from itertools import combinations
import codecs

class Class(object):
    def __init__(self, classID, name, parent):
        self.classID = classID
        self.name = name
        self.parent = parent
        self.radius = 5
        self.outline = "grey"
        self.fill = "gray"

    def toJSON(self):
        return json.dumps(self, ensure_ascii=False, default=lambda o: o.__dict__, sort_keys=True, indent=4).replace("\\n", "\n").replace("\\\"", "\"")

class Group(object):
    def __init__(self, name, parent, children, numChildrenNeeded=-1):
        self.name = name
        self.parent = parent
        self.radius = 6
        self.outline = "grey"
        self.fill = "gray"
        self.children = children
        self.numChildrenNeeded = numChildrenNeeded

    def toJSON(self):
        return json.dumps(self, ensure_ascii=False, default=lambda o: o.__dict__, sort_keys=True, indent=4).replace("\\n", "\n").replace("\\\"", "\"")
def generateJson(lines, parent):

    groupLevel = lines[0].count(">")
    groupName = lines[0].replace(">", "").rsplit(",", 1)[0].strip()
    # numChildrenNeeded = lines[0].rsplit(",", 1)[1].strip()
    children = []
    activeGroup = False
    activeGroupStart = 0
    lines = lines[1:]
    lines = list(filter(None, lines))
    for i in range(len(lines)):

        if activeGroup:
            if i < len(lines) - 1:
                if lines[i + 1].count(">") > 0 and lines[i + 1].count(">") < groupLevel:
                    print("Group Search: %s" % lines[i])
                    print("Group Search Second Line: %s" % lines[i + 1])
                    children += [Group(lines[i].replace(">", "").rsplit(",", 1)[0], groupName, generateJson(lines[activeGroupStart:i], lines[i].rsplit(",", 1)[1].strip()))]
                    activeGroup = False
                    return children
            else:
                print("second to last line: %s:" % lines[i])
                children += [Group(lines[i].replace(">", "").rsplit(",", 1)[0], groupName, generateJson(lines[activeGroupStart:i + 1], lines[i].rsplit(",", 1)[1].strip()))]
                activeGroup = False
                return children

        # if not activeGroup:
        else:
            if len(lines[i]) != 0:
                # print("Len: %d For: %s" % (len(lines[i]), lines[i]))
                if lines[i].count(">") > groupLevel:
                    print("Group Activated: %s:" % lines[i])
                    print(i)
                    # i = i - 1
                    activeGroup = True
                    activeGroupStart = i
                    groupLevel = lines[i].count(">")
                elif lines[i][0] == "-":
                    print("Class Added: %s:" % lines[i])
                    line = lines[i][2:].split(",")
                    classID = line[0].strip()
                    name = line[1][1:].strip()
                    children += [Class(classID, name, parent)]


def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__


# To add a thread, simply add an element to the list.
# Note that these strings are used to find the related txt files in the system.
threads = ["Devices", "Info Internetworks", "Intelligence", "Media",
           "Modeling and Simulation", "People", "Systems and Architecture", "Theory"]
# threads = ["Info Internetworks", "Intelligence"]

allFilesGood = True
for thread in threads:
    filename = thread + ".txt"
    if(os.path.isfile(filename)):
        goodFile = True
        with open(filename) as f:
            # empty = True
            lines = [x.strip() for x in f.readlines()]
            for line in lines:
                if line != "":
                    if line[0] != ">" and line[0] != "-":
                        goodFile = False
                        print("FAILED AT:%s: %s" % (line[0], str(line)))
                # else:
                #     empty = True
                #     print("Empty at:%s: %s" % (line[0], str(line)))
            # goodFile = goodFile and not empty
            goodFile = goodFile

        if goodFile:
            print("Found %s wich will be used for the thread \"%s\"" % (filename, thread))
        else:
            allFilesGood = False
            print("Found %s for \"%s\", but the file did not contain valid input.\nPlease read the formating guide and try again" % (filename, thread))
            print("Press Enter to Continue:")
            input()
    else:
        allFilesGood = False
        print("The file for \"%s\" was not found. %s was created. Please insert requirement data." % (thread, filename))
        f = open(filename, "w+")
        f.close()

if allFilesGood:
    for threadPair in combinations(threads, 2):
        filename = threadPair[0] + " >< " + threadPair[1] + ".json"

        with open(threadPair[0] + ".txt", "r") as f1:
            with open(threadPair[1] + ".txt", "r") as f2:
                linesOne = [x.strip() for x in f1.readlines()]
                linesTwo = [x.strip() for x in f2.readlines()]
                threadGroupOne = Group(threadPair[0], "Graduation", generateJson(linesOne, threadPair[0]), -1).toJSON()
                threadGroupTwo = Group(threadPair[1], "Graduation", generateJson(linesTwo, threadPair[1]), -1).toJSON()
                graduation = Group("Graduation", "null", [threadGroupOne, threadGroupTwo]).toJSON()
                print(graduation)
                # parsed = json.loads(graduation)
                # print(json.dumps(parsed, default=jdefault, indent=4, sort_keys=True))
                with codecs.open(filename, 'w', "utf-8") as outFile:
                    outFile.write(graduation)
                    # json.dump(graduation, outFile, ensure_ascii=False)
