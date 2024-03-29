import React, { useState, useEffect, Fragment } from 'react';
import axios from "axios";

import { timeToDay } from '../utils/Funcs.js';

// Firebase
import { getApps, initializeApp } from 'firebase/app';
import { getFirestore, collection, query, where, getDocs, orderBy, limit } from "firebase/firestore";
const firebaseConfig = {
  apiKey: "AIzaSyArjDv3hS4_rw1YyNz-JFXDX1ufF72bqr8",
  authDomain: "chooseone-105a9.firebaseapp.com",
  databaseURL: "https://chooseone-default-rtdb.firebaseio.com",
  projectId: "chooseone",
  storageBucket: "chooseone.appspot.com",
  messagingSenderId: "722704825746",
  appId: "1:722704825746:web:73f11551b9e59f4bc2d54b",
  measurementId: "G-YJ97DZH6V5"
};
var db = '';
if (!getApps().length){ 
  const firebaseApp = initializeApp(firebaseConfig);
  db = getFirestore(firebaseApp);
}else{
  db = getFirestore();
}

var categories = ['Love', 'News', 'Sports', 'Pastime', 'Health', 'Living', 'Career', 'Academics', 'IT'];
var tabColors = ['#ff69b4']
for(var i=1; i<11; i++) tabColors.push('hsla('+(i*100)+', 75%, 55%, 1)');

export default function Home (props) {

  const [todaysRanking, setTodaysRanking] = useState([]);

  useEffect(() => {
    let current=new Date();
    current=current.toJSON();
    var today = timeToDay(current.slice(0, 10));

    const q = query(collection(db, 'questions'), where('created_on', '==', today), orderBy('all_votes', 'desc'), limit(10));

    const promise = new Promise(function(resolve, reject) {
      resolve(getDocs(q));
    });
    promise.then((qq) => {
      var ques = [];
      Promise.all(qq.docs.map(doc => {
        ques.push(doc.data());
        return null;
      })).then(() => {
        setTodaysRanking(ques);
      });
    })
  }, [todaysRanking]);
  
  return (
    <Fragment>
      <div style={styles.left_side}>
        <h4 style={styles.semiTitle} className='cali'>Categories</h4>
        <ul>
          {categories.map((cate, idx) => (
            <li><a className='cali2' style={{ color: tabColors[idx] }} id="left{idx}" href={'/category/'+cate}>{cate}</a></li>
          ))}
        </ul>
        <h4 style={styles.semiTitle} className='cali'>Today's Ranking</h4>
        {todaysRanking.map((question, idx) => (
          <div className="side_question">
            <div className="title">
              {idx === 0 && (
                <Fragment>
                  <p style={{ fontSize: 25 }}>🥇</p> 
                  <a className="link" href={'/q/' + question.slug}><h6 style={{color: 'rgb(223, 176, 0)'}}><strong>{question.title}</strong></h6></a>
                </Fragment>
              )}
              {idx === 1 && (
                <Fragment>
                  <p style={{ fontSize: 25 }}>🥈</p>
                  <a className="link" href={'/q/' + question.slug}><h6 style={{color: 'rgb(174, 179, 181)'}}><strong>{question.title}</strong></h6></a>
                </Fragment>
              )}
              {idx === 2 && (
                <Fragment>
                  <p style={{ fontSize: 25 }}>🥉</p>
                  <a className="link" href={'/q/' + question.slug}><h6 style={{color: 'rgba(184, 115, 51, 0.692)'}}><strong>{question.title}</strong></h6></a>
                </Fragment>
              )}
              {idx !== 0 && idx !== 1 && idx !== 2 && (
                <Fragment>
                  <div style={styles.number}><p>{idx+1}</p></div>
                  <a className="link" href={'/q/' + question.slug}><h6>{question.title}</h6></a>
                </Fragment>
              )}
            </div>
            <ul>
              {question.choices.map(choice => (
                <div>
                  <label>○ {choice.choice_text}</label>
                  <br />
                </div>
              ))}
            </ul>
          </div>
        ))}
      </div>

    </Fragment>
  )
}

const styles = {
  left_side: {
    filter: 'drop-shadow(0px 0px 5px rgba(160, 160, 160, 0.7))',
    width: 200,
    marginRight: 30,
    backgroundColor: 'white',
    borderRadius: 15,
    paddingTop: 5,
    paddingBottom: 15,
    height: 'fit-content',
  },

  semiTitle: {
    paddingLeft: 10,
  },
  number: {
    width: 16,
    height: 16,
    borderRadius: 8,
    backgroundColor: 'rgb(2, 122, 255)',
    color: 'white',
    fontSize: 5,
    textAlign: 'center',
    marginTop: 7,
    marginRight: 4,
    marginLeft: 5,
  }
}