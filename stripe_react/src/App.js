import './index.css'
import React from 'react'
import { Elements } from '@stripe/react-stripe-js'
import { loadStripe } from "@stripe/stripe-js/pure"
import Subscription from "./Component/Subscription"
import Success from './Component/Success'
import Cancel from './Component/Cancel'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { REACT_APP_STRIPE_KEY } from './Config/config';

const stripe_key = REACT_APP_STRIPE_KEY
const stripePromise = loadStripe(stripe_key)

function App() {
  return (
   <>
   <Elements stripe={stripePromise} >
    <Router>
      <Routes>
      <Route exact path='subscription/' index element={<Subscription />} />
      <Route exact path='subscription/success/' element={<Success/>} />
      <Route exact path='subscription/failed/' element={<Cancel/>} />
      </Routes>
     </Router>
    
   </Elements>
   </>
  );
}

export default App;
