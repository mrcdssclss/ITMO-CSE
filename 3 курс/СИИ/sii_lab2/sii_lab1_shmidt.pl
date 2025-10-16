:- discontiguous married/3.
:- discontiguous divorced/3.

born(anna, 1979).
born(alexey, 1967).
born(alexandra, 2004).
born(andrey, 1975).
born(liliya, 1988).

born(galina, 1955).
born(vladimir, 1955).

born(darya, 1995).
born(dmitriy, 1995).

born(ilya, 1984).
born(mariya, 1989).
born(bogdan, 2015).
born(alina, 2006).

born(lubov, 1957).
born(viktor2, 1957).
born(alexandr, 1956).
born(viktor1, 1956).

born(natalya, 1960).
born(sergey, 1959).

born(nina, 1981).
born(igor, 1979).
born(polina, 2006).
born(grigoriy, 2015).

born(alevtina, 1950).
born(mihail, 1950).
born(elena, 1970).
born(alena, 1990).
born(osman, 2017).
born(ekaterina, 1995).
born(artem, 1993).
born(nikita, 2006).

died(viktor1, 2010).
died(alexandr, 2023).

married(anna, andrey, 2002).
divorced(anna, andrey, 2010).
married(anna, alexey, 2012).
married(andrey, liliya, 2016).

married(darya, dmitriy, 2020).
married(mariya, ilya, 2015).

married(lubov, alexandr, 1976).
divorced(lubov, alexandr, 1986).
married(lubov, viktor1, 1990).
divorced(lubov, viktor1, 2010).
married(lubov, viktor2, 2014).

married(natalya, sergey, 1980).
married(nina, igor, 2000).
divorced(nina, igor, 2010).

married(alevtina, mihail, 1970).
married(elena, alexey, 1990).
divorced(elena, alexey, 2000).
married(ekaterina, artem, 2022).

married(galina, vladimir, 1974)

alive(Person, Year) :-
    born(Person, Born),
    Year >= Born,
    (died(Person, Dead) ->  Year < Dead ; true).

older(Person1, Person2) :-
    born(Person1, Born1),
    born(Person2, Born2),
    Born1 < Born2.

younger(Person1, Person2) :-
    born(Person1, Born1),
    born(Person2, Born2),
    Born1 > Born2.

age(Person, Year, Age) :-
    born(Person, Born),
    Year >= Born,
    Age is Year - Born,
    (died(Person, Died) -> Year < Died ; true).

are_married(Person1, Person2, Year) :-
    married(Person1, Person2, Marriage),
    Year >= Marriage,
    (divorced(Person1, Person2, Divorced) ->  Year < Divorced ; true).

same_age(Person1, Person2) :-
    born(Person1, Year1),
    born(Person2, Year2),
    Year1 = Year2.

age_diff(Person1, Person2, Age) :-
    born(Person1, Year1),
    born(Person2, Year2),
    Age is abs(Year1 - Year2).

can_be_parent(Person1, Person2):-
    born(Person1, Year1),
    born(Person2, Year2),
    abs(Year1-Year2) > 18.
        
child(Person, Year):-
    born(Person, Born),
    (Year - Born) < 18.

are_divorced(Person1, Person2, Year) :-
    married(Person1, Person2, Marriage),
    divorced(Person1, Person2, Divorce),
    Year >= Divorce, 
    Divorce > Marriage.
