import time
import pyautogui
import simple_colors
import sys
import random
import traceback

def convert_res(xcoords, ycoords):
    x1 = int(round(xcoords[0]*.75, 0))
    x2 = int(round(xcoords[1]*.75, 0))
    y1 = int(round(ycoords[0]*.75, 0))
    y2 = int(round(ycoords[1]*.75, 0))

    xcoords = (x1, x2)
    ycoords = (y1, y2)
    return xcoords, ycoords

def mouse_functions(coord_info, button='left'):
    xcoord, ycoord, duration = coord_info
    pyautogui.moveTo(xcoord, ycoord, duration)
    pyautogui.click(button = button)

def get_coords(xcoords, ycoords, duration):
    convert = False
    if convert:
        xcoords, ycoords = convert_res(xcoords, ycoords)
    first_xcoord = xcoords[0]
    second_xcoord = xcoords[1]
    first_ycoord = ycoords[0]
    second_ycoord = ycoords[1]
    first_duration = duration[0]
    second_duration = duration[1]

    xcoord = random.randrange(first_xcoord, second_xcoord, 1)
    ycoord = random.randrange(first_ycoord, second_ycoord, 1)
    duration = round(random.uniform(first_duration, second_duration), 1)

    return xcoord, ycoord, duration

def smithing_darts():
    try:
        x = 0
        while True:
            coord_info = get_coords((1255, 1310), (601, 665), (.3, .7))
            print("Clicking Forge.")
            mouse_functions(coord_info)

            coord_info = get_coords((1392, 1660), (908, 928), (.7, 1.1))
            print("Clicking 'Begin Project'.")
            mouse_functions(coord_info)

            coord_info = get_coords((1208, 1222), (678, 722), (.5, 1.2))
            print("Clicking anvil.")
            mouse_functions(coord_info)

            duration = round(random.uniform(34, 35.5), 1)
            time.sleep(duration)
            x += 1
            if x == 1:
                print(simple_colors.cyan(f"Ran {x} time\n"))
            else:
                print(simple_colors.cyan(f"Ran {x} times\n"))
    except:
        #print(traceback.format_exc())
        print(simple_colors.green(f"\nCreated {x * 50} rune darts!"))

def smithing_bars():
    try:
        x = 0
        while True:
            coord_info = get_coords((1227, 1327), (759, 859), (.5, .9))
            print("Clicking Furnace.")
            mouse_functions(coord_info)

            coord_info = get_coords((896, 1000), (913, 932), (.7, 1.1))
            print("Clicking 'Deposit all materials'.")
            mouse_functions(coord_info)

            coord_info = get_coords((1392, 1660), (908, 928), (.7, 1.1))
            print("Clicking 'Begin Project'.")
            mouse_functions(coord_info)

            duration = round(random.uniform(50.5, 52), 1)
            time.sleep(duration)
            x += 1
            if x == 1:
                print(simple_colors.cyan(f"Ran {x} time\n"))
            else:
                print(simple_colors.cyan(f"Ran {x} times\n"))
    except:
        #print(traceback.format_exc())
        print(simple_colors.green(f"\nCreated around {x*(27 + 2)} rune bars!"))

def bankRun(material):
    try:
        if material != "Rune":
            #Cell door click
            print("Clicking cell door")
            coord_info = get_coords((1881, 1895), (1053, 1080), (.7, 1.1))
            mouse_functions(coord_info)
            time.sleep(round(random.uniform(3.1, 4), 1))

            #Rune ore click
            print("Going to rune area")
            duration = round(random.uniform(.5, 1), 1)
            pyautogui.moveTo(2368 ,230, duration)
            pyautogui.click(button='left')
            time.sleep(round(random.uniform(7.5, 9.5), 1))

        #Go to ladder
        print("Going to ladder")
        coord_info = get_coords((680, 732), (612, 646), (.4, .7))
        mouse_functions(coord_info)
        time.sleep(round(random.uniform(3.0, 3.7), 1))

        #Click ladder
        print("Clicking ladder")
        coord_info = get_coords((1200, 1206), (690, 722), (.5, .9))
        mouse_functions(coord_info)
        time.sleep(round(random.uniform(2.8, 3.5), 1))

        #Go to workshop
        print("Going to workshop")
        duration = round(random.uniform(.7, 1.1), 1)
        pyautogui.moveTo(2525, 157, duration)
        pyautogui.click(button='left')
        time.sleep(round(random.uniform(7.5, 9), 1))

        #Clicking Furnace
        print("Clicking furnace")
        coord_info = get_coords((1227, 1327), (770, 870), (.5, .9))
        mouse_functions(coord_info)
        time.sleep(round(random.uniform(.7, 1.2), 1))

        #Depositing Materials
        print("Depositing ore")
        coord_info = get_coords((896, 1000), (913, 932), (.7, 1.1))
        mouse_functions(coord_info)
        time.sleep(round(random.uniform(.5, 1.2), 1))
        
        #Go to dungeon entrance
        print("Going to dungeon entrance")
        duration = round(random.uniform(.7, 1.1), 1)
        pyautogui.moveTo(2353, 164, duration)
        pyautogui.click(button='left')
        time.sleep(round(random.uniform(7, 9), 1))

        #Clicking ladder
        print("Clicking ladder")
        coord_info = get_coords((1095, 1130), (600, 660), (.4, .8))
        mouse_functions(coord_info)
        time.sleep(round(random.uniform(2.8, 3.5), 1))

        #Going to rune ore
        print("Going to rune area")
        coord_info = get_coords((1838, 1867), (770, 823), (.4, .7))
        mouse_functions(coord_info)
        time.sleep(round(random.uniform(1.5, 2.5), 1))
        #Clicking/mining rune
        
        if material != "Rune":
            #Going to cell door
            print("Going to cell door")
            duration = round(random.uniform(.7, 1.1), 1)
            pyautogui.moveTo(2508, 93, duration)
            pyautogui.click(button='left')
            time.sleep(round(random.uniform(7.5, 9.5), 1))

            #Clicking cell door
            print("Clicking cell door")
            coord_info = get_coords((1246, 1318), (587, 608), (.4, .8))
            mouse_functions(coord_info)
            time.sleep(round(random.uniform(3.1, 4), 1))

            #Going to Luminite
            print("Going to luminite ore")
            coord_info = get_coords((691, 735), (383, 431), (.4, .8))
            mouse_functions(coord_info)
            time.sleep(round(random.uniform(3.6, 4.3), 1))

            #Clicking Luminite
            #mine_luminite()
            print("Clicking luminite")
    except:
        print(f"Stopping {material} bank run.")

def mine_rune():
    start = time.time()
    try:
        runs = 0
        while True:
            boxFills = 0
            while boxFills <= 4:
                staminaRegen = 0
                coord_info = get_coords((1283, 1350), (772, 830), (.5, .9))
                print("Mining rune.")
                while staminaRegen <= 8:
                    mouse_functions(coord_info)
                    time.sleep(round(random.uniform(26.5, 29), 1))
                    staminaRegen += 1
                pyautogui.click(button='left')
                time.sleep(round(random.uniform(19.5, 22), 1))
                coord_info = get_coords((2332, 2360), (650, 673), (.5, .9))
                print("Filling ore box.")
                mouse_functions(coord_info)
                boxFills += 1
            print("Ore box full.")
            invFill = 0
            coord_info = get_coords((1283, 1350), (772, 830), (.5, .9))
            while invFill <= 7:
                mouse_functions(coord_info)
                time.sleep(round(random.uniform(26.5, 29), 1))
                invFill += 1
            runs += 1
            print(simple_colors.blue(f"Runs: {runs}."))
    except:
       end = time.time()
       print(simple_colors.green(f"\nMined around {int((end - start)/7)} rune!"))

def mine_luminite():
    start = time.time()
    try:
        runs = 0
        while True:
            boxFills = 0
            while boxFills <= 3:
                staminaRegen = 0
                coord_info = get_coords((1131, 1212), (620, 703), (.5, .9))
                print("Mining luminite.")
                while staminaRegen <= 5:
                    mouse_functions(coord_info)
                    time.sleep(round(random.uniform(24.5, 28.5), 1))
                    staminaRegen += 1
                pyautogui.click(button='left')
                time.sleep(round(random.uniform(20, 23.7), 1))
                coord_info = get_coords((2332, 2360), (650, 673), (.5, .9))
                print("Filling ore box.")
                mouse_functions(coord_info)
                boxFills += 1
            invFill = 0
            coord_info = get_coords((1131, 1212), (620, 703), (.5 ,.9))
            while invFill <= 3:
                mouse_functions(coord_info)
                time.sleep(round(random.uniform(24.5, 28.5), 1))
                invFill += 1
            runs += 1
            print(simple_colors.blue(f"Runs: {runs}"))
    except:
        end = time.time()
        #print(traceback.format_exc())
        print(simple_colors.green(f"\nMined around {int((end - start)/7)} luminite!"))

def main():
    try: 
        args = sys.argv[1:]
        #print(args[1])
        if args[0].lower() == 'smith':
            if args[1].lower() == 'bars':
                smithing_bars()
            elif args[1].lower() == 'darts':
                smithing_darts()
            else:
                print("Not yet implemented for smithing skill.")
        elif args[0].lower() == 'mine':
            if args[1].lower() == 'luminite':
                mine_luminite()
            elif args[1].lower() == 'rune':
                mine_rune()
            else:
                print("Not yet implemented")
        elif args[0].lower() == 'test':
            #bankRun("Rune")
            print(convert_res((1000, 2560), (1000, 1440)))
        else:
            print("Skill not yet implemented")
     
    except KeyboardInterrupt:
        print("Ending auto clicker.")

if __name__ == "__main__":
    main()
