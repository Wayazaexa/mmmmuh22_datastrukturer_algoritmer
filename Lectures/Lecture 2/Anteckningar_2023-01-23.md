# Anteckningar 2023-01-23

## Inlämningsuppgift. Inlämning 1 - Del 1.
 
 - Beskrivning finns i Omniway.
 - Inlämning sker genom länk till git repository (Codeberg eller Github)
 - En bonusuppgift (en extra poäng till tentan).

## C++ Skapa objekt på stacken vs med new (på heap) 

```
myClass * B;

void func_A() {
   myClass A = myClass(input);

  B = &A;  // Kommer inte vara åtkommlig när vi lämnar funktionen.
  return; 
}
```

```
myClass * B;

void func_A() {
   myClass * A = new myClass(input);

  B = A;
  delete A;  //Om vi inte kör delete finns objektet kvar.
  return; 
}
```

## Smart pointers i C++
Sedan C++11, 2011

https://www.geeksforgeeks.org/smart-pointers-cpp/

## Iterera

```
for n in my_list:
  
```

### << overloading

```
Temperature t;

// Kod

cout << "Dagens temperatur << t << endl;

t.print();
```

https://learn.microsoft.com/en-us/cpp/standard-library/overloading-the-output-operator-for-your-own-classes?view=msvc-170


