import ollama

def testonce():
    res = ollama.chat(
        model="llava",
        messages=[
            {
                'role': 'user',
                'content': 'Describe this image:',
                'images': ['./jmb.jpg']
            }
        ]
    )
    print(res['message']['content'])

for i in range(10):
    testonce()
