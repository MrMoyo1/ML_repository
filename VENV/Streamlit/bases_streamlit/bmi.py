import streamlit as st
st.title("Welcome to the BMI Calculator")

weight = st.number_input('Enter your weight in kgs')
status = st.radio('Select your heigth format:',('cms','meters','feet'))
try: 

    if status == 'cms':
        height = st.number_input('cms')
        bmi = weight/((height/100)**2)

    elif status == 'meters':
        height = st.number_input('meters')
        bmi = weight/((height)**2)

    else: 
        height = st.number_input('feet')
        bmi = weight/((height/3.28)**2)
except:
    print('Zero division error')
try :
    if(st.button('Calculate BMI')):
        st.write('Your BMI index is {}'.format(round(bmi)))

        if bmi < 16 :
            st.error('YOU SKINI ASS MTF !')
        elif (bmi >=16 and bmi<18.5):
            st.warning('You good man !')
        elif (bmi >=18.5 and bmi<25):
            st.success('be careful !')
        elif (bmi >=25 and bmi<30):
            st.warning('YOU FAT ASS')
        else:
            st.error('YOU gotta get to the GYM !')
except:
    print('are u a f*cking alien ?')