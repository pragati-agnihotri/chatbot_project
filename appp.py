from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is(.*)',['hi %1']],
    ['(hi|hello|hey|holla|hola)',['hey there' ,'hi there','haayyy']],
    ['(.*) in (.*) is fun',['%1 in %2 is indeed fun']],
    ['(.*) your name ?',['J.A.R.V.I.S']]
]

my_dummy_reflections={
    'go':'gone',
    'hello':'hey there'
}

chat =Chat(pairs,my_dummy_reflections)
chat.converse()