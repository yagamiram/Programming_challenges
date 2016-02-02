        '''
        Insertion Sort
        Aprroach: 
        Like how we play cards game.
        Pick a card and find its position.
        i.e You have bunch of cards in left hand.
        A new card in the right hand.
        Now the new card should be placed in the correct postion in the left hand.
        Step 1: Add the new card in the last position of the bunch of already sorted cards in the left hand.
        step 2: Now compare it with adjacent loaction and if the adjacent cards is greater then swap
        step 3: It it is not greater then which means the card is placed in the right location.
        '''
        def insertion_sort(numbers):
            if len(numbers) == 0:
                return []
            else:
                idx = 1
                while idx <= len(numbers)-1:
                    # check the number from 0 to idx-1
                    idy = idx-1
                    idz = idx
                    while idy >= 0:
                        if numbers[idy] > numbers[idz]:
                            numbers[idy], numbers[idz] = numbers[idz], numbers[idy]
                            idz -= 1
                        else:
                            break
                        idy -= 1
                    idx += 1
            print numbers
        insertion_sort([5,6,7,3,4,77,87,2,13,43,2442,5,3,24,5,25,24,5,2,4,6,1,3])
