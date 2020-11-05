from firebase import firebase
firebase = firebase.FirebaseApplication('https://ukb-educationalconsultant.firebaseio.com/',None)
database= firebase.get('/ukb/','')
