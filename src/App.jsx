import { useEffect, useState } from "react";
import "./App.css";
export default function App() {
  const [fakeData, setFakeData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:400/quantity=10")
      .then((res) => res.json())
      .then((data) => setFakeData(data))
      .catch((err) => console.error(err));
  }, []);
  return (
    <section>
      {fakeData.map((data) => (
        <article key={data.id}>
          <header>
            <h4>
              {data.name}
              <span>{data.lastName}</span>
              <small>{data.age}</small>
            </h4>
          </header>
          <p>{data.comment}</p>
        </article>
      ))}
    </section>
  );
}
