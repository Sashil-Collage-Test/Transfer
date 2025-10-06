import { initializeApp } from 'firebase/app';
import { getFirestore, connectFirestoreEmulator } from 'firebase/firestore';
import { getStorage, connectStorageEmulator } from 'firebase/storage';

const firebaseConfig = {
  apiKey: process.env.REACT_APP_FIREBASE_API_KEY || "AIzaSyBtGWIKi4h1nH_Wn2YX3mFEeiA561B3ffI",
  authDomain: process.env.REACT_APP_FIREBASE_AUTH_DOMAIN || "dropbeam-file-sharing-platform.firebaseapp.com",
  projectId: process.env.REACT_APP_FIREBASE_PROJECT_ID || "dropbeam-file-sharing-platform",
  storageBucket: process.env.REACT_APP_FIREBASE_STORAGE_BUCKET || "dropbeam-file-sharing-platform.appspot.com",
  messagingSenderId: process.env.REACT_APP_FIREBASE_MESSAGING_SENDER_ID || "211202935789",
  appId: process.env.REACT_APP_FIREBASE_APP_ID || "1:211202935789:web:78d5adde5917fa755735e4"
};

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const storage = getStorage(app);

// Connect to emulators in development
if (process.env.NODE_ENV === 'development' && process.env.REACT_APP_USE_EMULATORS === 'true') {
  try {
    connectFirestoreEmulator(db, 'localhost', 8080);
    connectStorageEmulator(storage, 'localhost', 9199);
  } catch (error) {
    console.log('Emulators already connected or not available');
  }
}

export default app;