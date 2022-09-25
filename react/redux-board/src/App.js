import './App.css';
import { useSelector, useDispatch } from 'react-redux';
import { useState } from 'react';
import { addPost, deletePost } from './features/Posts';


function App() {
  const [name, setName] = useState("")
  const [content, setContent] = useState("")
  // state.posts.valueそれぞれはposts.jsを確認
  const postList = useSelector((state) => state.posts.value)
  // console.log(postList)

  const dispatch = useDispatch()

  

  const handleClick = () => {
    dispatch(
      addPost({
        id: postList.length+1,
        name: name,
        content: content,
      })
      )
      setName("")
      setContent("")
      console.log(setName)
  }

  return (
    <div className="App">
      <div>
        <h1>掲示板</h1>
      </div>
      <div className='addPost'>
        <input type="text" placeholder='名前' onChange={(e) => setName(e.target.value)} value={name} />
        <input type="text" placeholder='内容' onChange={(e) => setContent(e.target.value)} value={content} />
        <button onClick={() => handleClick()}>投稿</button>
        <hr />
      </div>
      <div className='displayPosts'>
        {postList.map((post) => (
          <div key={post.id} className="post">
            <h1 className='postName'>{post.name}</h1>
            <h1 className='postContent'>{post.content}</h1>
            {/* ここでいうidはposts.js内のaction.payloadのid */}
            <button onClick={() => dispatch(deletePost({ id: post.id })) } >削除</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
