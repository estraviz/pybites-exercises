import pytest

from convert_chars import convert_pybites_chars


@pytest.mark.parametrize("arg, expected", [
    ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do",
     "LorEm IPSum dolor SIT amET, conSEcTETur adIPIScIng ElIT, SEd do"),
    ("Vestibulum morbi blandit cursus risus at ultrices",
     "VESTIBulum morBI BlandIT curSuS rISuS aT ulTrIcES"),
    ("Aliquet nibh praesent tristique magna sit amet purus gravida quis",
     "AlIquET nIBh PraESEnT TrISTIquE magna SIT amET PuruS gravIda quIS"),
    ("Fames ac turpis egestas maecenas pharetra",
     "FamES ac TurPIS EgESTaS maEcEnaS PharETra"),
    ("Vitae purus faucibus ornare suspendisse sed nisi lacus",
     "VITaE PuruS faucIBuS ornarE SuSPEndISSE SEd nISI lacuS"),
    ("Pharetra massa massa ultricies mi quis",
     "pharETra maSSa maSSa ulTrIcIES mI quIS"),
    ("Senectus et netus et malesuada fames",
     "sEnEcTuS ET nETuS ET malESuada famES"),
    ("Arcu non sodales neque sodales ut etiam sit",
     "Arcu non SodalES nEquE SodalES uT ETIam SIT"),
    ("Natoque penatibus et magnis dis parturient montes nascetur",
     "NaToquE PEnaTIBuS ET magnIS dIS ParTurIEnT monTES naScETur"),
    ("Urna cursus eget nunc scelerisque viverra mauris in aliquam",
     "Urna curSuS EgET nunc ScElErISquE vIvErra maurIS In alIquam"),
    ("Vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt",
     "VESTIBulum maTTIS ullamcorPEr vElIT SEd ullamcorPEr morBI TIncIdunT"),
    ("Tempus urna et pharetra pharetra",
     "tEmPuS urna ET PharETra PharETra"),
    ("Ullamcorper a lacus vestibulum sed",
     "UllamcorPEr a lacuS vESTIBulum SEd"),
    ("Cursus risus at ultrices mi",
     "CurSuS rISuS aT ulTrIcES mI"),
    ("Egestas congue quisque egestas diam in arcu",
     "egESTaS conguE quISquE EgESTaS dIam In arcu"),
    ("Sit amet tellus cras adipiscing enim eu",
     "sIT amET TElluS craS adIPIScIng EnIm Eu"),
    ("Imperdiet sed euismod nisi porta lorem mollis aliquam",
     "imPErdIET SEd EuISmod nISI PorTa lorEm mollIS alIquam"),
    ("Adipiscing tristique risus nec feugiat in fermentum posuere urna",
     "AdIPIScIng TrISTIquE rISuS nEc fEugIaT In fErmEnTum PoSuErE urna"),
    ("Et magnis dis parturient montes",
     "eT magnIS dIS ParTurIEnT monTES"),
    ("Elementum curabitur vitae nunc sed velit dignissim sodales ut.",
     "elEmEnTum curaBITur vITaE nunc SEd vElIT dIgnISSIm SodalES uT."),
])
def test_convert_pybites_chars(arg, expected):
    assert convert_pybites_chars(arg) == expected
