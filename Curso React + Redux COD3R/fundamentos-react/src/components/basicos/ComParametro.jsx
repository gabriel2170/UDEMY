import React from "react"


export default function ComParametro(props) {
   
    return (
        <div>
            <h2>{props.titulo}</h2>
            <strong>{props.aluno} tem nota {props.nota}</strong>
        </div>
    )

}