relieves(crocin, headache).
relieves(gelusil, nausea).
relieves(wikoril, cough).
relieves(eno, acidity).

aggravates(salted_chips, high_blood_pressure).
aggravates(butter_chicken, diabetes).

should_take(Person, Drug) :- complains_of(Person, Symptom), relieves(Drug, Symptom), not(unsuitable_for(Person, Drug)).
unsuitable_for(Food, Person) :- aggravates(Food, Condition), suffers_from(Person, Condition).

complains_of(patient_name, acidity).
suffers_from(patient_name, diabetes).
