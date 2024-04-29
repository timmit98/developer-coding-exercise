export async function fetchPost(slug) {
  try {
    const res = await fetch(`http://localhost:3001/posts/${slug}/`); //ideally not hardcoded but needs must
    const data = res.json();
    return data;
  } catch (err) {
    return {};
  }
}
