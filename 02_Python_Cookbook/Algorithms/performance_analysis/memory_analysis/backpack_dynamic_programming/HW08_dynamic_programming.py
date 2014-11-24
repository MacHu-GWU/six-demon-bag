#coding=utf-8
import time
st = time.clock()
et = time.clock()

''' === initial the data === '''
SUBJECT_FILENAME = "testsubject.txt"
SUBJECT_FILENAME = "subjects.txt"

VALUE, WORK = 0, 1

### === Problem 1: Building A Subject Dictionary ===

def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    
    subjects = {} ## initial dict
    inputFile = open(filename)
    for line in inputFile:
        line = line.replace(' ','')
        line = line.replace('\n','')
        temp = line.split(',')
        temp[1]=int(temp[1])
        temp[2]=int(temp[2])
        subjects[float(temp[0])]=tuple(temp[1:3])
    return subjects
        
def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    
    res = 'Course\tValue\tWork\n======\t=====\t====\n'
    subNames = list(subjects.keys())
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + str(s) + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)
    return None

### Problem 2: Subject Selection By Greedy Optimization

##''' === how to use function name as an input variable ==='''
##def plus(a,b):
##    return a+b
##
##def minus(a,b):
##    return a-b
##
##def mutiply(a,b):
##    return a*b
##
##def pickmode(a,b,mode):
##    ans = mode(a,b)
##    return ans
##
##print(pickmode(3,2,plus))

## small module 1
''' === compare Value, Work, Ratio === '''
def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

##print(cmpValue(subjects[2.01],subjects[2.02]))
##print(cmpWork(subjects[2.01],subjects[2.02]))
##print(cmpRatio(subjects[2.01],subjects[2.02]))

## small module 2
''' === sort course by Value, Work and Ratio ==='''
def invert_by_Value(d):
    'invert dict by Value'
    inverse = dict()
    for key in d:
        val = d[key]
        i = val[0]
        if i not in inverse:
            inverse[i] = [key]
        else:
            inverse[i].append(key)
    keylist = list(inverse.keys())
    keylist.sort(reverse=True)
    return inverse,keylist

def invert_by_Work(d):
    'invert dict by Work'
    inverse = dict()
    for key in d:
        val = d[key]
        i = val[1]
        if i not in inverse:
            inverse[i] = [key]
        else:
            inverse[i].append(key)
    keylist = list(inverse.keys())
    keylist.sort()
    return inverse,keylist

def invert_by_Ratio(d):
    'invert dict by Ratio'
    inverse = dict()
    for key in d:
        val = d[key]
        i = val[0]/val[1]
        if i not in inverse:
            inverse[i] = [key]
        else:
            inverse[i].append(key)
    keylist = list(inverse.keys())
    keylist.sort(reverse=True)
    return inverse,keylist

def SortBy_ValueWork_or_Ratio(subjects,mode):
    ''' 3 mode to chooe, they are:
    invert_by_Ratio
    invert_by_Ratio
    invert_by_Ratio

    Complexity: most time are spent on invert the dict
    2 * number of the key, linear level
    '''
    (invSubjects,valueList)=mode(subjects)
    sortedCourse = list()
    for val in valueList:
        for course in invSubjects[val]:
            sortedCourse.append(course)
    return sortedCourse

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    
    === example ===
    For instance, if we're given the following subject dictionary
    smallCatalog, and a maximum of 15 hours of work:

    # name value work

    {'6.00': (16, 8),
    
'1.00':
(7 ,
7),
    
'6.01':
(5 ,
3),
    
'15.01':
(9,
6)}
    
    greedyAdvisor(smallCatalog, 15, cmpValue) 
    {'6.00': (16, 8), '15.01': (9, 6)}
    greedyAdvisor(smallCatalog, 15, cmpWork)
    {'6.01': (5, 3), '15.01': (9, 6)}
    greedyAdvisor(smallCatalog, 15, cmpRatio)
    {'6.00': (16, 8), '6.01': (5, 3)}
    """
    
    greedyChoice = dict()
    valueEarned = 0
    workSpend = maxWork
    sortedCourse = SortBy_ValueWork_or_Ratio(subjects,comparator)
    for i in sortedCourse:
        if subjects[i][1] <= maxWork: ## check if time allowed
            greedyChoice[i] = subjects[i] ## record choice
            maxWork = maxWork - subjects[i][1] ## subtract taken work time
            valueEarned = valueEarned + subjects[i][0]
    workSpend = workSpend - maxWork
    ratio = valueEarned/workSpend
    print('you earned', valueEarned, 'credit')
    print('you spend', workSpend, 'hours on study')
    print('your working efficiency is: ', ratio)
    print('you still have', maxWork, 'hour to study.')    
    return greedyChoice

## Problem 3: bruteForceAdvisor
def invert_by_Work_and_limit(d,maxWork):
    ## 限制最大的Work，然后从1 - maxwork 排序
    ## 对于work = 1 本身，内部并不排序
    'invert dict by Work, and the maxWork limit'
    inverse = dict()
    for key in d:
        val = d[key]
        i = val[1]
        if i <= maxWork:
            if i not in inverse:
                inverse[i] = [key]
            else:
                inverse[i].append(key)
    keylist = list(inverse.keys())
    keylist.sort()
    print keylist
    'generate the sorted course list'
    sortedCourse = list() 
    for val in keylist:
        for course in inverse[val]:
            sortedCourse.append(course)
#     print sortedCourse
    return sortedCourse #筛选出选择最小的

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    ## answerList 的第i个元素是 空间上限为i的最优解
    ## answerList 的第i个元素是 [{6.0: (10, 1)}, 10]， 第一个元素是 解的字典，第二个元素是分数总和
    answerList = [[{},0]] ## !! initial Final Answer
    for i in range(1,maxWork+1):
        bruteAns = {} ## initial answer
        bruteVal = 0 ## initial value
        sortedCourse = invert_by_Work_and_limit(subjects,i)
#         print len(sortedCourse)
        for test in sortedCourse:
#             print test, subjects[test]
#             print '==========================='
#             print test, answerList[i - subjects[test][1]][0]
            ## check if test is already in given answer
            
            ## answerList[]
            if test not in answerList[i - subjects[test][1]][0]:
                totalvalue = subjects[test][0] + answerList[i - subjects[test][1]][1]               
                ## check if this solution better than existing one
                if totalvalue > bruteVal:
                    bruteVal = totalvalue
                    bruteAns = answerList[i - subjects[test][1]][0].copy()
                    bruteAns[test] = subjects[test]
        answerList.append([bruteAns,bruteVal])
        print answerList
    return answerList

''' ============================= testing ============================= '''
subjects = loadSubjects(SUBJECT_FILENAME) ## initial
printSubjects(subjects) ## initial
timeToStudy = 15

''' === answer test === '''
##print(greedyAdvisor(subjects, timeToStudy, invert_by_Value))
##print(greedyAdvisor(subjects, timeToStudy, invert_by_Work))
##print(greedyAdvisor(subjects, timeToStudy, invert_by_Ratio))

for i in invert_by_Work_and_limit(subjects, 15):
    print subjects[i]

# answerList = bruteForceAdvisor(subjects, timeToStudy)
# print 'smart answer is: ',answerList[timeToStudy]

''' === performance test === '''
' greedychoice '
##st = time.clock()
##for t in range(1,timeToStudy+1):
##    answer = greedyAdvisor(subjects, timeToStudy, invert_by_Ratio)
##et = time.clock()
##print(et-st)
##' === dp brute '
##st = time.clock()
##answerList = bruteForceAdvisor(subjects, timeToStudy)
##et = time.clock()
##print(et-st)
