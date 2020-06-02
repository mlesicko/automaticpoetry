from forms.haiku import HaikuForm
from forms.because import BecauseForm
from forms.acrostic import AcrosticForm
from forms.atoz import AtozForm
from forms.rhymingcouplet import RhymingCoupletForm
from forms.iambicpentameter import IambicPentameterForm
from forms.limerick import LimerickForm
from forms.alliterative import AlliterativeForm
from forms.ihate import IHateForm
from forms.roses import RosesForm
from forms.tanka import TankaForm
from forms.iambicpentameter_strict import IambicPentameterStrictForm
from forms.markov import MarkovForm
from forms.markov2 import Markov2Form
from forms.markovsounds import MarkovSoundsForm
from forms.all import AllForm
from forms.generate_dataset import GenerateDatasetForm
from forms.speedtest import SpeedtestForm

poem_forms = ["haiku","because","acrostic","atoz","couplet",
        "iambicpentameter","limerick","alliterative", "ihate",
        "roses","tanka","iambicpentameter_strict"]

tool_forms = ["all","generate_dataset","speedtest"]

other_forms = ["markov","markov2","markovsounds"]

def getForm(form):
    ## POEMS
    if form==poem_forms[0]:
        return HaikuForm()
    elif form==poem_forms[1]:
        return BecauseForm()
    elif form==poem_forms[2]:
        return AcrosticForm()
    elif form==poem_forms[3]:
        return AtozForm()
    elif form==poem_forms[4]:
        return RhymingCoupletForm()
    elif form=="rhymingcouplet":
        return RhymingCoupletForm()
    elif form==poem_forms[5]:
        return IambicPentameterForm()
    elif form==poem_forms[6]:
        return LimerickForm()
    elif form==poem_forms[7]:
        return AlliterativeForm()
    elif form==poem_forms[8]:
        return IHateForm()
    elif form==poem_forms[9]:
        return RosesForm()
    elif form==poem_forms[10]:
        return TankaForm()
    elif form==poem_forms[11]:
        return IambicPentameterStrictForm()
    ## TOOLS
    elif form==tool_forms[0]:
        return AllForm()
    elif form==tool_forms[1]:
        return GenerateDatasetForm()
    elif form==tool_forms[2]:
        return SpeedtestForm()
    ## OTHER THINGS
    elif form==other_forms[0]:
        return MarkovForm()
    elif form==other_forms[1]:
        return Markov2Form()
    elif form==other_forms[2]:
        return MarkovSoundsForm()
    else:
        return None

