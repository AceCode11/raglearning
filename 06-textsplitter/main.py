from langchain_text_splitters import CharacterTextSplitter

text = """
SimpleText is the native text editor for the Apple classic Mac OS.[1] SimpleText allows text editing and text formatting (underline, italic, bold, etc.), fonts, and sizes. It was developed to integrate the features included in the different versions of TeachText that were created by various software development groups within Apple Computer.[2]

It can be considered similar to Windows' WordPad application. In later versions, it also gained additional read-only display capabilities for PICT files, as well as other Mac OS built-in formats like Quickdraw GX and QTIF, 3DMF and even QuickTime movies.[2] SimpleText can even record short sound samples and, using Apple's PlainTalk speech system, read out text in English. Users wanting to add sounds longer than 24 seconds, however, needed to use a separate program to create the sound and then paste the desired sound into the document using ResEdit.[2]

SimpleText superseded TeachText, which was included in System Software up until it was replaced in 1994 (shipped with System Update 3.0 and System 7.1.2). The need for TeachText arose after Apple stopped bundling MacWrite, to ensure that every user could open and read Readme documents.
"""
splitter =  CharacterTextSplitter(
    chunk_size = 100 , 
    chunk_overlap = 0, 
    separator=' ' 
)

result = splitter.split_text(text)
print(result)