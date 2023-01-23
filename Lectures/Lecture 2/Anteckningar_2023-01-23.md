# Anteckningar 2023-01-23

## Inlämningsuppgift. Inlämning 1 - Del 1.
 
 - Beskrivning finns i Omniway.
 - Inlämning sker genom länk till git repository (Codeberg eller Github)
 - En bonusuppgift (en extra poäng till tentan).

### Inlämning Bonusuppgift 

mylist: 1->2->3->4->5->6

mylist.swap(1,3);

Efter:
mylist: 1->4->3->2->5->6


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


## C++ bygge

### Google test

Om ni använder MSYS2 / MINGW64 finns det ett färdigt paket att installera:https://packages.msys2.org/package/mingw-w64-x86_64-gtest

```
$pacman -S mingw-w64-x86_64-gtest
```

I er tasks.json fil måste ni lägga in följande under "tasks"->"args":

```
                "-I",
                "C:/GoogleTest/googletest/googletest/include",
                "-I",
                "C:/GoogleTest/googletest/bin",
                "-L",
                "C:/GoogleTest/googletest/lib/Debug",
                "-lgtest",
                "-lgtest_main"
```
<!--
### CMake

Öppna MSYS MINGW64. Installera följande:

```
pacman -S mingw-w64-x86_64-cmake
pacman -S ninja
```

Installera CMake extension i Visual studio code.
-->