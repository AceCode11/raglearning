from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict  , Annotated , Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#schema

class Review(TypedDict):
    key_themes : Annotated[list[str] , 'Write down all the key theme discussed in the review in the list']
    pros : Annotated[Optional[list[str]] , 'Write down all the pros inside the list']
    cons : Annotated[Optional[list[str]] , 'Write down all the cons inside the list']
    summary : Annotated[str , 'A brief summary of the review']
    sentiment : Annotated[str , 'Return sentiment of the review either postive . negative , neutral']



structured_model = model.with_structured_output(Review)
result = structured_model.invoke('''After spending two weeks with the Horizon Prime X, I can confidently say it represents a massive leap forward for mobile technology, 
                                 though it arrives with a premium price tag that will make most buyers hesitate.From the moment you pick it up, the matte titanium chassis 
                                 feels incredibly luxurious and premium, completely eliminating annoying fingerprint smudges. Turning it on reveals the stunning 6.9-inch 
                                 Dynamic OLED panel; its variable refresh rate makes everything from simple UI animations to fast-paced mobile gaming look incredibly fluid 
                                 and bright, even under direct sunlight.Performance is blistering fast, driven by the latest octa-core chipset. App switching is seamless, 
                                 and multitasking with split-screen windows doesn't cause a single stutter. However, that extreme processing power comes at a cost. 
                                 During extended gaming sessions or 4K video recording, the device suffers from aggressive thermal throttling, making the upper glass 
                                 back uncomfortably warm to the touch. Fortunately, the massive battery easily compensates for this high power draw, comfortably providing a 
                                 solid day and a half of heavy usage, backed by impressive ultra-fast charging capabilities.The camera department is where this phone truly shines,
                                  yet simultaneously stumbles. The primary 200MP sensor captures breathtaking details and rich, vibrant colors during daylight. Night mode is equally spectacular, 
                                 turning pitch-black environments into well-lit, sharp images. Unfortunately, the 10x telephoto zoom lens is a massive disappointment. Images pushed past 5x zoom rapidly 
                                 lose clarity, turning into a noisy, pixelated mess. Furthermore, the accompanying AI image-processing software frequently over-saturates skin tones, making people look 
                                 unnaturally orange.On the software front, the custom user interface is clean, highly customizable, and completely free of annoying bloatware. The promised seven years of 
                                 operating system updates offer incredible long-term value. Ultimately, while the premium pricing and minor camera inconsistencies might deter casual users, the Horizon Prime X 
                                 stands out as an absolute powerhouse for tech enthusiasts who demand top-tier battery life, a gorgeous display, and blazing-fast speeds.
''')

print(result['key_themes'])
print(result['pros'])
print(result['cons'])
print(result['summary'])
print(result['sentiment'])


