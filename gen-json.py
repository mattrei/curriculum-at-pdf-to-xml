import copy
import os
import sys

import xmltodict
import json

FOLDER = sys.argv[1]

STANDARDS = FOLDER + os.sep + 'LearningStandardDocuments.xml'
LESSONS = FOLDER + os.sep + 'Lessons.xml'
ITEMS = FOLDER + os.sep + 'LearningStandardItems.xml'
RESOURCES = FOLDER + os.sep + 'LearningResources.xml'

def read_xmls():
    standards = {}
    lessons = {}
    items = {}
    ressources = {}

    print('Reading LearningStandardDocuments from {}'.format(STANDARDS))
    with open(STANDARDS, 'r') as f:
        standards = xmltodict.parse(f.read())

    print('Reading Lessons from {}'.format(LESSONS))
    with open(LESSONS, 'r') as f:
        lessons = xmltodict.parse(f.read())

    print('Reading LearningStandardItems from {}'.format(ITEMS))
    with open(ITEMS, 'r') as f:
        items = xmltodict.parse(f.read())

    print('Reading LearningResources from {}'.format(RESOURCES))
    with open(RESOURCES, 'r') as f:
        resources = xmltodict.parse(f.read())

    return (standards, lessons, items, resources)

def create_lessons(lessons_obj, items, resources):

    lessons = copy.deepcopy(lessons_obj)

    for lesson in lessons['Lessons']['Lesson']:
        print("\nLessons {}".format(lesson['Title']))

        try:
            litems = []
            for refid in get_list(lesson['LearningStandards']['LearningStandardItemRefId']):
                for item in items['LearningStandardItems']['LearningStandardItem']:
                    if refid == item['@RefId']:
                        litems.append(item)
            lesson['LearningStandards'] = litems
        except KeyError:
            pass

        try:
            lresources = []
            for refid in get_list(lesson['LearningResources']['LearningResourceRefId']):
                for resource in resources['LearningResources']['LearningResource']:
                    if refid == resource['@RefId']:
                        lresources.append(resource)
            lesson['LearningResources'] = lresources
        except KeyError:
            pass

    return lessons

def create_standards(standards_obj, items):

    standards = copy.deepcopy(standards_obj)

    for standard in standards['LearningStandardDocuments']['LearningStandardDocument']:
        print("\nStandard {}".format(standard['Title']))

        refid = standard['LearningStandardItemRefId']
        sitems = []

        for item in items['LearningStandardItems']['LearningStandardItem']:
            if refid == item['@RefId']:
                sitems.append(item)
                add_item_successor(refid, items, sitems)

        standard['LearningStandardItems'] = sitems
    return standards

def add_item_successor(refid, items, sitems):
    for item in items['LearningStandardItems']['LearningStandardItem']:
        try: 
            for preitem in get_list(item['PredecessorItems']['LearningStandardItemRefId']):
                if refid == preitem:
                    sitems.append(item)
                    add_item_successor(item["@RefId"], items, sitems)
        except KeyError:
            pass


def get_list(obj):
    if isinstance(obj, str):
        return [obj]
    else:
        return obj

if __name__ == '__main__':

    (standards, lessons, items, resources) = read_xmls()

    new_lessons = create_lessons(lessons, items, resources)
    with open(sys.argv[1] + '-lessons.json', 'w') as f:
        json.dump(new_lessons, f, indent=2)

    new_standards = create_standards(standards, items)
    with open(sys.argv[1] + '-standards.json', 'w') as f:
        json.dump(new_standards, f, indent=2)
