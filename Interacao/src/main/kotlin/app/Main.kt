package app

import javax.swing.JOptionPane.showInputDialog
import javax.swing.JOptionPane.showMessageDialog

open class Main {
    companion object {
        @JvmStatic fun main(args: Array<String>) {

            showMessageDialog(null, "alguem está usando este pc?")
            var confirmacao:Int = showInputDialog(null,"Se alguem estiver usando este pc, digite 1").toInt()

            if (confirmacao == 1) {
                showMessageDialog(null, "Obrigado pela confirmacao")
            }

        }
    }
}