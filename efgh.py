import streamlit as st
from urllib.request import urlopen
from lxml import etree

links=['https://devfolio.co/submissions/connectme-3', 'https://devfolio.co/submissions/treatment-chain', 'https://devfolio.co/submissions/at-your-door', 'https://devfolio.co/submissions/order-and-chaos', 'https://devfolio.co/submissions/mediblock', 'https://devfolio.co/submissions/open-market', 'https://devfolio.co/submissions/student-playbook', 'https://devfolio.co/submissions/jagrukkissan', 'https://devfolio.co/submissions/fashionai', 'https://devfolio.co/submissions/healthquick', 'https://devfolio.co/submissions/smer-smart-medical-electronic-records', 'https://devfolio.co/submissions/the-detector', 'https://devfolio.co/submissions/decentralizedstockmarket', 'https://devfolio.co/submissions/mentos', 'https://devfolio.co/submissions/smart-helmet-1', 'https://devfolio.co/submissions/smart-231', 'https://devfolio.co/submissions/zomateen-1', 'https://devfolio.co/submissions/genz-insurance', 'https://devfolio.co/submissions/hydrochain', 'https://devfolio.co/submissions/elixir-3', 'https://devfolio.co/submissions/healthchain', 'https://devfolio.co/submissions/course-mash', 'https://devfolio.co/submissions/project-salamander-a-gift-recommendation-system', 'https://devfolio.co/submissions/secai', 'https://devfolio.co/submissions/daignos', 'https://devfolio.co/submissions/summaryscape', 'https://devfolio.co/submissions/petify', 'https://devfolio.co/submissions/bet-on-better', 'https://devfolio.co/submissions/sharehub', 'https://devfolio.co/submissions/merry-cacti-1', 'https://devfolio.co/submissions/shuttle-1', 'https://devfolio.co/submissions/finity-1', 'https://devfolio.co/submissions/netknot', 'https://devfolio.co/submissions/antidepression-talk-bot-1', 'https://devfolio.co/submissions/url-shortner-1', 'https://devfolio.co/submissions/good-pods', 'https://devfolio.co/submissions/the-platform', 'https://devfolio.co/submissions/healthfirst', 'https://devfolio.co/submissions/smart-checkout', 'https://devfolio.co/submissions/find-ridr', 'https://devfolio.co/submissions/leskollab', 'https://devfolio.co/submissions/handwritten-text-ocr', 'https://devfolio.co/submissions/snoozeloose', 'https://devfolio.co/submissions/vahak', 'https://devfolio.co/submissions/survonthego', 'https://devfolio.co/submissions/pypep-toolbox-cli-and-gui-tools-for-biotechies', 'https://devfolio.co/submissions/attendance-using-facial-recognition', 'https://devfolio.co/submissions/darechange', 'https://devfolio.co/submissions/enhancinator', 'https://devfolio.co/submissions/finance-tracker', 'https://devfolio.co/submissions/smart-parking-app', 'https://devfolio.co/submissions/standnote-1', 'https://devfolio.co/submissions/perfect-parking-lot', 'https://devfolio.co/submissions/buho', 'https://devfolio.co/submissions/cospaces', 'https://devfolio.co/submissions/attendance-tinder', 'https://devfolio.co/submissions/seevid', 'https://devfolio.co/submissions/smart-agriculture-ffd3', 'https://devfolio.co/submissions/shelldrop-05a8', 'https://devfolio.co/submissions/devchassy', 'https://devfolio.co/submissions/clippy-easy-to-share', 'https://devfolio.co/submissions/cancer-detector-with-doctor-recommendation', 'https://devfolio.co/submissions/e-learning-app', 'https://devfolio.co/submissions/tldw-too-long-didnt-watch', 'https://devfolio.co/submissions/homelyfitness', 'https://devfolio.co/submissions/actual-retail-price-system-1', 'https://devfolio.co/submissions/wynk-hire', 'https://devfolio.co/submissions/tripmate', 'https://devfolio.co/submissions/the-helix', 'https://devfolio.co/submissions/todo-task-management-web-app', 'https://devfolio.co/submissions/age-well', 'https://devfolio.co/submissions/target-1', 'https://devfolio.co/submissions/jobfirm-find-job-anytime-anywhere', 'https://devfolio.co/submissions/blog-app-6', 'https://devfolio.co/submissions/supergrowth-3', 'https://devfolio.co/submissions/anytime-healthcare-kit', 'https://devfolio.co/submissions/leanr', 'https://devfolio.co/submissions/hermes', 'https://devfolio.co/submissions/enable', 'https://devfolio.co/submissions/dossier', 'https://devfolio.co/submissions/neuralaid-1', 'https://devfolio.co/submissions/cororun-1', 'https://devfolio.co/submissions/gamers-galaxy', 'https://devfolio.co/submissions/anxidote', 'https://devfolio.co/submissions/criclive', 'https://devfolio.co/submissions/vfit', 'https://devfolio.co/submissions/project-manna', 'https://devfolio.co/submissions/respace-1', 'https://devfolio.co/submissions/workify-3', 'https://devfolio.co/submissions/your-moody-friend', 'https://devfolio.co/submissions/medical-blocks', 'https://devfolio.co/submissions/newsalyzer', 'https://devfolio.co/submissions/crscndo', 'https://devfolio.co/submissions/amigo-1', 'https://devfolio.co/submissions/lecast', 'https://devfolio.co/submissions/apni-mandi', 'https://devfolio.co/submissions/dtechtives', 'https://devfolio.co/submissions/arcade', 'https://devfolio.co/submissions/git-meet', 'https://devfolio.co/submissions/decentralised-indoor-navigation', 'https://devfolio.co/submissions/signteract', 'https://devfolio.co/submissions/answer-evaluation-1', 'https://devfolio.co/submissions/adblock-tv-adbtv', 'https://devfolio.co/submissions/que-14', 'https://devfolio.co/submissions/twinni-extension', 'https://devfolio.co/submissions/dbuz', 'https://devfolio.co/submissions/soothsayer', 'https://devfolio.co/submissions/bookshelf', 'https://devfolio.co/submissions/zeropass', 'https://devfolio.co/submissions/mow-motion-over-web', 'https://devfolio.co/submissions/beast-mode', 'https://devfolio.co/submissions/pwnhub', 'https://devfolio.co/submissions/krishi-unnati-1', 'https://devfolio.co/submissions/sevashop', 'https://devfolio.co/submissions/election-proctor', 'https://devfolio.co/submissions/price-prediction-market', 'https://devfolio.co/submissions/guerilla-lock-security', 'https://devfolio.co/submissions/parke-3', 'https://devfolio.co/submissions/teleport', 'https://devfolio.co/submissions/cheerup', 'https://devfolio.co/submissions/quick-grader', 'https://devfolio.co/submissions/pictionary', 'https://devfolio.co/submissions/medhub-4', 'https://devfolio.co/submissions/wardrobe', 'https://devfolio.co/submissions/mapme-3', 'https://devfolio.co/submissions/agro-31', 'https://devfolio.co/submissions/attendifyai-based-attendances-system', 'https://devfolio.co/submissions/happy-gardening', 'https://devfolio.co/submissions/learnai-1', 'https://devfolio.co/submissions/motive-detector', 'https://devfolio.co/submissions/cookie-the-doggie-your-new-bestie-1', 'https://devfolio.co/submissions/org-research', 'https://devfolio.co/submissions/cuisiner', 'https://devfolio.co/submissions/prepup', 'https://devfolio.co/submissions/eyed', 'https://devfolio.co/submissions/payup-carpool-expense-tracker', 'https://devfolio.co/submissions/michi', 'https://devfolio.co/submissions/gestrol', 'https://devfolio.co/submissions/workouthome', 'https://devfolio.co/submissions/teamforhack', 'https://devfolio.co/submissions/paw']
public_funds=0
devfolio_funds=0
pub_dict={}
dev_dict={}
@st.cache(ttl=3600)
def f(links):
    public_funds=0
    devfolio_funds=0
    pub_dict={}
    dev_dict={}
    for j in links:
        response=urlopen(j)
        #driver.get(j)
        htmlparser=etree.HTMLParser()
        tree=etree.parse(response,htmlparser)
        pub_fund=((tree.xpath("//*[@id=\"root\"]/div/div[2]/section/div[2]/div[2]/div/div[3]/div[1]/span/span")[0].text))
        no=int((pub_fund).replace(',',''))
        pub_dict[j]=no
        #pub_fund=driver.find_elements_by_xpath("//*[@id=\"root\"]/div/div[2]/section/div[2]/div[2]/div/div[3]/div[1]/span/span")
        #no=int((pub_fund[0].text).replace(',',''))
        public_funds=no+public_funds
        dev_fund=((tree.xpath("//*[@id=\"root\"]/div/div[2]/section/div[2]/div[2]/div/div[3]/div[2]/span/span")[0].text))
        no2=int((dev_fund).replace(',',''))
        dev_dict[j]=no2
        #dev_fund=driver.find_elements_by_xpath("//*[@id=\"root\"]/div/div[2]/section/div[2]/div[2]/div/div[3]/div[2]/span/span")
        #no2=int((dev_fund[0].text).replace(',',''))
        devfolio_funds=devfolio_funds+no2
    return pub_dict,dev_dict,devfolio_funds,public_funds
pub_dict,dev_dict,devfolio_funds,public_funds=f(links)
links1=[]
for i in links:
    links1.append(i.replace('https://devfolio.co/submissions/',''))
project=st.sidebar.selectbox("Project",links1)
st.markdown("# Overall")
st.markdown("## Public Funding:"+str(public_funds))
st.markdown("## Devfolio Funding:"+str(devfolio_funds))
st.markdown("# Project:"+project)
st.markdown("## Public Funding:"+str(pub_dict['https://devfolio.co/submissions/'+project]))
st.markdown("## Devfolio Funding:" + str(dev_dict['https://devfolio.co/submissions/'+project]))
cad=st.slider("Number you think the next donation will be",1,50000)
abra=dev_dict['https://devfolio.co/submissions/'+project]
st.markdown("Total donation is likely to be(If current devfolio matching isn't 0:"+str(((((((abra+public_funds)**0.5)+(cad**0.5)))**2)-public_funds-cad)))
st.markdown("Application data updates every 30 minutes")



