import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import org.antlr.v4.runtime.misc.*;
import java.util.*;
import java.io.*;

public class Compute extends ComputationBaseListener {
	int lastExit = 0;
        @Override public void enterFormula(ComputationParser.FormulaContext ctx) {
	}
        @Override public void exitFormula(ComputationParser.FormulaContext ctx) {
	}

	public int getResult() {
		return lastExit;
	}

	public static void main(String[] args) throws Exception {
		ANTLRInputStream input = new ANTLRInputStream(System.in);
		ComputationLexer lexer = new ComputationLexer(input);
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		ComputationParser parser = new ComputationParser(tokens);
		ParseTree tree = parser.formula();
		ParseTreeWalker walker = new ParseTreeWalker();

		Compute listener = new Compute();
		walker.walk(listener, tree);
		System.out.println(listener.getResult());
	}
}