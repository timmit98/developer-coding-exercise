import Head from "next/head";
import { fetchPost } from "../../scripts/fetchPost";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import ReactMarkdon from "react-markdown";

export default function BlogPost() {
  const [JSONPostObject, setposts] = useState({});
  const router = useRouter();
  const { slug } = router.query;
  useEffect(() => {
    const dataFromApiCall = async () => {
      try {
        const response = await fetchPost(slug);
        setposts(response);
      } catch (error) {
        console.log("Error Fetching Data");
      }
    };
    dataFromApiCall();
  }, [slug]);

  const post = JSONPostObject.post;

  return (
    <div>
      <Head>
        <title></title>
      </Head>
      <main>
        <div>
          {post ? (
            <div>
              <h1>{post.title}</h1>
              <p>
                <strong>Author:</strong> {post.author}
              </p>
              <ReactMarkdon>{post.content}</ReactMarkdon>
              <p>
                <strong>Tags:</strong> {post.tags.join(", ")}
              </p>
            </div>
          ) : (
            <p>Data Missing?!</p>
          )}
        </div>
      </main>
    </div>
  );
}
