import Head from "next/head";
import Link from "next/link";
import { fetchPosts } from "../scripts/fetchPosts";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";

export default function Home() {
  const [JSONPostObject, setposts] = useState({});
  const router = useRouter();

  const handleClick = (postId) => {
    router.push(`/posts/${postId}`);
  };

  useEffect(() => {
    const dataFromApiCall = async () => {
      try {
        const response = await fetchPosts();
        setposts(response);
      } catch (error) {
        console.log("Error Fetching Data");
      }
    };
    dataFromApiCall();
  }, []);

  const posts = JSONPostObject.post;

  return (
    <div>
      <Head>
        <title>Blogging Platform</title>
      </Head>
      <main>
        {posts ? (
          <ul>
            {posts.map((post, index) => (
              <li key={index}>
                <span
                  onClick={() => handleClick(post.slug)}
                  style={{
                    cursor: "pointer",
                    color: "blue",
                    textDecoration: "underline",
                  }}
                >
                  {post.title}
                </span>
              </li>
            ))}
          </ul>
        ) : (
          <p>No posts available</p>
        )}
      </main>
    </div>
  );
}
