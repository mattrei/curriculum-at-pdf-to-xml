import copy
import os
import sys
from os import listdir
from os.path import isfile, join

import xmltodict
import json


def read_xmls(folder):
    STANDARDS = folder + os.sep + 'LearningStandardDocuments.xml'
    LESSONS = folder + os.sep + 'Lessons.xml'
    ITEMS = folder + os.sep + 'LearningStandardItems.xml'
    RESOURCES = folder + os.sep + 'LearningResources.xml'
    standards = {}
    lessons = {}
    items = {}
    resources = {}

    try:
        with open(STANDARDS, 'r') as f:
            standards = xmltodict.parse(f.read())

        with open(LESSONS, 'r') as f:
            lessons = xmltodict.parse(f.read())

        with open(ITEMS, 'r') as f:
            items = xmltodict.parse(f.read())

        with open(RESOURCES, 'r') as f:
            resources = xmltodict.parse(f.read())
    except FileNotFoundError as e:
        print('Error in ' + folder)

    return (standards, lessons, items, resources)

def create_lessons(lessons_obj, items, resources):

    lessons = copy.deepcopy(lessons_obj)

    for lesson in lessons['Lessons']['Lesson']:
        #print("\nLessons {}".format(lesson['Title']))

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
        #print("\nStandard {}".format(standard['Title']))

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

    model = { 
            'LearningStandardDocuments': [],
            'Lessons': [] 
            }

    p = '.'
    folders = [f for f in listdir(p) if not isfile(join(p, f)) and f != 'schema']

    for folder in folders:
        print('reading ' + folder)
        try:
            (standards, lessons, items, resources) = read_xmls(folder)
            new_lessons = create_lessons(lessons, items, resources)
            new_standards = create_standards(standards, items)

            model['Lessons'].extend(new_lessons['Lessons']['Lesson'])
            model['LearningStandardDocuments'].extend(new_standards['LearningStandardDocuments']['LearningStandardDocument'])
        except Exception as e:
            print ('error processing')
            print(e)

    with open('model.json', 'w') as f:
        json.dump(model, f, indent=2)
