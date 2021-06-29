import pandas as ps

'''
Add:
- Latest 50 crash dates(you can sort this by PERSON_TYPE)
- Sort by PERSON_TYPE
- Get the Total Crashes/Crashes by PERSON_TYPE ratio(you can also have ratios between two differen PERSON_TYPE values)
- Get crashes by STATE(you can also get their ratio between them)
- Get crashes by SEX ratio (M/F (non-binary people too(???)))
- Create a new temporary DataFrame by crash date(and then get the crashes per month ratio for all the states)
- Car crashes by year

You can create temporary DataFrames by sorting(as same as shown in the BTK videos(with proper methods fulfilling this purpose))
'''

class Commander:
    #data = ps.read_csv('./Traffic_Accidents_Presentation/traffic-crashes-people-1.csv')
    try:
        data = ps.read_csv('./traffic-crashes-people-1.csv')
    except:
        data = ps.read_csv('./Traffic_Accidents_Presentation/traffic-crashes-people-1.csv')
    df = ps.DataFrame(data)

    def totalCarCrashes(self,year:int=None):
        if year == None:
            print(f"\n\n{len(self.df.index)}\n\n")
        elif 2013 <= year <=2019:
            self.df['CRASH_YEAR'] = self.df['CRASH_DATE'].str.split(' ')
            dates = [i[0] for i in self.df['CRASH_YEAR']]
            years = []
            for i in dates:
                currentYear = int(i.split('/')[2])
                if currentYear == year:
                    years.append(currentYear)

            print(f"\n\n{len(years)} Car Crashes in {year}\n\n")
        else:
            print('\n\nThis year is invalid in the database, please try again...\n\n')

    def latestCarCrashes(self):
        for crash in self.df['CRASH_DATE'].head(50):
            print(f'\n{crash}\n')       

    def rolesInCrashes(self):
        for personType in self.df['PERSON_TYPE'].unique():
            print(f'\n{personType}\n')

    def totalAndRolesRatio(self):
        self.rolesInCrashes()
        decision = input('Which role would you like to go with(copy/paste from up ahead)?\n')
        for personType in self.df['PERSON_TYPE'].unique():
            if decision == personType:
                totalCrashes = len(self.df.index)
                print(f'\n\n{totalCrashes} total crashes')
                crashesByRole = len(self.df[self.df['PERSON_TYPE'] == personType].index)
                print(f'{crashesByRole} {personType.capitalize()} crashes')
                print(f'\n "Total/{personType.capitalize()}" Ratio: {round(totalCrashes/crashesByRole, 2)}\n')
                break
        else:
            print('Role chosen is not valid in the database')

    def crashesOfState(self):
        for state in self.df["STATE"].unique():
            print(f'{state}\n')
        stateChosen = input('Which state would you like to go with(copy/paste your selection)?\n')
        for stateType in self.df['STATE'].unique():
            if stateChosen == stateType:
                crashes = len(self.df[self.df["STATE"] == stateChosen].index)
                print(f'\n{crashes} crashes for {stateChosen}\n')
                break
        else:
            print('\n State chosen is not valid inside the database(maybe miscopied?)\n')
        
    def crashesRatioState(self):
        for state in self.df["STATE"].unique():
            if state != 'nan':
                print(f'{state}\n')
        stateChosen = input('Which state would you like to go with(copy/paste your selection)?\n')
        for stateType in self.df['STATE'].unique():
            if stateChosen == stateType:
                temporaryDataFrame = self.df.dropna(how="any", subset=["STATE"], inplace=False)
                totalCrashes = len(temporaryDataFrame.index)
                print(f'\n\n{totalCrashes} total crashes')
                crashesByState = len(self.df[self.df['STATE'] == stateType].index)
                print(f'{crashesByState} {stateType} crashes')
                print(f'\n "Total/{stateType}" Ratio: {round(totalCrashes/crashesByState, 2)}\n')
                break
        else:
            print('\n State chosen is not valid inside the database(maybe miscopied?)\n')

    def crashesperMonthForStates(self):
        self.df['CRASH_YEAR'] = self.df['CRASH_DATE'].str.split(' ')
        dates = [i[0] for i in self.df['CRASH_YEAR']]
        lastDate = int(dates[0].split('/')[2])
        firstDate = int(dates[-1].split('/')[2])
        yearSpan = (lastDate - firstDate) + 1
        #print(yearSpan)
        for state in self.df["STATE"].unique():
            if state != 'nan':
                print(f'{state}\n')
        stateChosen = input('Which state would you like to go with(copy/paste your selection)?\n')
        for stateType in self.df['STATE'].unique():
            if stateChosen == stateType:
                crashesByState = len(self.df[self.df['STATE'] == stateType].index)
                print(f'\n{crashesByState} {stateType} crashes')
                print(f'\n{yearSpan} years considered')
                print(f'\n {round(crashesByState/(yearSpan * 12), 2)} crashes per month for {stateType}\n')
                break
        else:
            print('\n State chosen is not valid inside the database(maybe miscopied?)\n')

    def crashesbySex(self):
        for gender in self.df["SEX"].unique():
            if gender != 'nan':
                if gender == 'U':
                    print('Unknown(U)\n')
                elif gender == 'X':
                    print('Non-Binary(X)\n')
                elif gender == 'M':
                    print('Male(M)\n')
                elif gender == 'F':
                    print('Female(F)\n')
        genderChosen = input('Which gender would you like to go with(copy/paste the symbols)?\n')
        for genderType in self.df['SEX'].unique():
            if gender == genderType:
                crashes = len(self.df[self.df["SEX"] == genderChosen].index)

                if genderChosen == 'U':
                    print(f'\n{crashes} crashes for People whose gender info is unidentified\n')
                elif genderChosen == 'X':
                    print(f'\n{crashes} crashes for Non-Binary People\n')
                elif genderChosen == 'M':
                    print(f'\n{crashes} crashes for Males\n')
                elif genderChosen == 'F':
                    print(f'\n{crashes} crashes for Females\n')
                break
        else:
            print('\n State chosen is not valid inside the database(maybe miscopied?)\n')

    def crashesbySexRatio(self):
        for gender in self.df["SEX"].unique():
            if gender != 'nan':
                if gender == 'U':
                    print('Unknown(U)\n')
                elif gender == 'X':
                    print('Non-Binary(X)\n')
                elif gender == 'M':
                    print('Male(M)\n')
                elif gender == 'F':
                    print('Female(F)\n')
        genderChosenLeft = input('First gender selection(copy/paste the symbols): ')
        genderChosenRight = input('Second gender selection(copy/paste the symbols):')
        for gender1 in self.df["SEX"].unique():
            if genderChosenLeft == gender1:
                for gender2 in self.df["SEX"].unique():
                    if genderChosenRight == gender2:
                        firstGenderCrashes = len(self.df[self.df["SEX"] == genderChosenLeft].index)
                        secondGenderCrashes = len(self.df[self.df["SEX"] == genderChosenRight].index)
                        print(f'\n{firstGenderCrashes} crashes by {genderChosenLeft}\n')
                        print(f'{secondGenderCrashes} crashes by {genderChosenRight}\n')
                        print(f'{round(firstGenderCrashes/secondGenderCrashes, 2)} is the {genderChosenLeft}/{genderChosenRight} crash ratio\n')
                        break
                else:
                    print('\n Invalid in the database, try again.\n')
                break
        else:
            print('\n Invalid in the database, try again.\n')


myCommander = Commander()
while True:
    command = input('0 - Exit\n1 - Total Car Crashes\n2 - Latest 50 Car Crashes\n3 - Roles\n4 - Ratio of Total/Role(You Define)\n5 - Crashes by State\n6 - Ratio Crashes by State\n7 - Crashes per Month for States\n8 - Crashes by Sex\n9 - Crash Ratio by Sex\nResponse: ')
    if command == '0':
        break
    elif command == '1':
        yearChosen = int(input('\nWhich year would you like to go with(available from 2013 to 2019): '))
        print('\n\n')
        myCommander.totalCarCrashes(yearChosen)
        input('Press ENTER when you wish to continue: ')
        print('\n\n')
    elif command == '2':
        print('\n\n')
        myCommander.latestCarCrashes()
        input('Press ENTER when you wish to continue: ')
        print('\n\n')
    elif command == '3':
        print('\n\n')
        myCommander.rolesInCrashes()
        input('Press ENTER when you wish to continue: ')
        print('\n\n')
    elif command == '4':
        print('\n\n')
        myCommander.totalAndRolesRatio()
        input('Press ENTER when you wish to continue: ')
        print('\n\n')
    elif command == '5':
        print('\n\n')
        myCommander.crashesOfState()
        input('Press ENTER when you wish to continue: ')
        print('\n\n')
    elif command == '6':
        print('\n\n')
        myCommander.crashesRatioState()
        input('Press ENTER when you wish to continue: ')
        print('\n\n')
    elif command == '7':
        print('\n\n')
        myCommander.crashesperMonthForStates()
        input('Press ENTER when you wish to continue: ')
        print('\n\n')
    elif command == '8':
        print('\n\n')
        myCommander.crashesbySex()
        input('Press ENTER when you wish to continue: ')
        print('\n\n')
    elif command == '9':
        print('\n\n')
        myCommander.crashesbySexRatio()
        input('Press ENTER when you wish to continue: ')
        print('\n\n')
    else:
        print('\nMistyped, please type a valid option.\n')


