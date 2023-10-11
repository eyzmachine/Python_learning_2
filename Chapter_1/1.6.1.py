classes = dict()

def get_ancestor(anc, desc):
    if classes.keys().__contains__(desc) and anc == desc:
        return True
    if not classes.keys().__contains__(desc):
        return False
    else:
        if list(classes[desc]).__contains__(anc):
            return True
        else:
            decision = False
            for cl in classes[desc]:
                decision = get_ancestor(anc, cl)
                if decision:
                    return decision
            return decision
    

def graphs():
    n = int(input())
    while n > 0:
        input_classes = input()
        split_classes = list(map(str.strip, input_classes.split(":")))
        if split_classes.__len__() == 1:
            classes[split_classes[0]] = list()
        else:
            classes[split_classes[0]] = split_classes[1].split(' ')
        n -= 1
    
    q = int(input())
    while q > 0:
        input_classes = input()
        split_classes = list(map(str.strip, input_classes.split(' ')))
        ancestor = split_classes[0]
        descendant = split_classes[1]
        print("Yes" if get_ancestor(ancestor, descendant) else "No")
        q -= 1
        
graphs()


