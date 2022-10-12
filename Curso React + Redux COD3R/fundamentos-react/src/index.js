import React from 'react'
import ReactDOM from 'react-dom'
import Primeiro from './components/basicos/Primeiro'
import ComParametro from './components/basicos/ComParametro'
import './index.css'

const tag = <h1>Hello</h1>

ReactDOM.render(
  <div>
    <Primeiro></Primeiro>
    <ComParametro titulo="Segundo Componente" aluno='Gabriel' nota={6.5}/>
  </div>
  ,
  document.getElementById('root')


)