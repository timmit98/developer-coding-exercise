import Head from 'next/head';
import {fetchPost} from '../scripts/fetchPost';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

export default function BlogPost() {
  const [JSONPostObject, setposts] = useState({});
  const router = useRouter();
    
  useEffect(() => {
    const dataFromApiCall = async () => {
      try 
      {
        const response = await fetchPost(slug);
        setposts(response);
      }
      catch (error) {
        console.log('Error Fetching Data');
      }
    };
  dataFromApiCall()
  }, []);

  console.log(JSONPostObject)
  const posts = JSONPostObject.post
  
  return (
    <div>
      <Head>
        <title></title>
      </Head>
      <main>
      </main>
    </div>
  );
}
