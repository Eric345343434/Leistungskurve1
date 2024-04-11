def bubble_sort(arr):
 
    n = len(arr)
    swapped = False  # Optimierung: Wenn keine Vertauschungen erfolgen, ist das Array bereits sortiert
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Elemente vertauschen, wenn sie in der falschen Reihenfolge sind
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            # Wenn keine Vertauschungen vorgenommen wurden, die Hauptschleife verlassen
            break



    

    