#!/usr/bin/env python3
"""
`keyboard` implementation and driver

@authors:
"""

import pathlib

def spell_check(filename: str) -> None:
    """Rank words by their proximity to the target"""
    # TODO: Implement this function
    alphabet = {'a':[2,1],'b':[1,5],'c':[1,3],'d':[2,3],'e':[3,3],'f':[2,4],'g':[2,5],'h':[2,6],'i':[3,8],'j':[2,7],'k':[2,8],'l':[2,9],'m':[1,7],'n':[1,6],'o':[3,9],'p':[3,10],'q':[3,1],'r':[3,4],'s':[2,2],'t':[3,5],'u':[3,7],'v':[1,4],'w':[3,2],'x':[1,2],'y':[3,6],'z':[1,1]}
    f = open(filename,'r')
    lines=f.read().splitlines()
    ntests = int(lines[0])
    linecounter = 1
    for a in range(ntests): #one loop for each typed word
        nchecksstring = ''
        for letter in lines[linecounter]:
            try:
                nchecksstring += str(int(letter))
            except:
                pass
        nchecks = int(nchecksstring)
        results = {}
        word = lines[linecounter][0:-2]
        linecounter += 1
        for n in range(nchecks): #one loop is one word to test against the input word
            tester = lines[linecounter]
            linecounter += 1
            worddistance = 0
            for l in range(len(tester)): #one loop is a letter in each tester word
                hdistance = abs(alphabet[word[l]][1]-alphabet[tester[l]][1])
                vdistance = abs(alphabet[word[l]][0]-alphabet[tester[l]][0])
                letterdistance = hdistance+vdistance
                worddistance += letterdistance
            results[tester] = worddistance
        sorted_results = sorted(results.items(), key=lambda x: (x[1],x[0]))
        for item in sorted_results:
            print(f'{item[0]} {item[1]}')
    f.close
    ...


def main():
    """Entry point"""
    filename = "sample.in.txt"
    if not pathlib.Path(filename).exists():
        filename = f"projects/keyboard/{filename}"
    spell_check(filename)


if __name__ == "__main__":
    main()
