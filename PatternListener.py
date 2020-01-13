from JavaParserListener import JavaParserListener
from antlr4 import *
import settings


class PatternListener(JavaParserListener):
    """[this child class PatternListener is used to process all classes and methods which are related to either visitor or listener pattern]

    Arguments:
        JavaParserListener {[class]} -- [JavaParserListener is a parent class created by antlr4 and being inherited here]
    """

    # Enter a parse tree produced by JavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx):
        """[this method is used to process all the method declarations in the repository]

        Arguments:
            ctx {[type]} -- [overriding method gives the object of the parse tree node i.e., JavaParser.MethodDeclarationContext]
        """
        method_name = ctx.IDENTIFIER().getText()
        if method_name not in ['enterRule', 'exitRule', 'visitRule']:
            method_def_len = len(ctx.methodBody().getText()) - 2
            method_overriden_flag = ''
            if ctx.OVERRIDEN() is not None:
                method_overriden_flag = ctx.OVERRIDEN().getText()

            # _considering only overriden methods and starting with either enter, exit or visit
            if method_def_len > 0 and method_overriden_flag == '@Override':
                for target_method in settings.target_method_list:
                    if method_name.startswith(target_method) and len(method_name) > len(target_method):
                        settings.method_list.append(method_name)

                        # _add repective X part to respective target method list
                        if method_name.startswith('enter'):
                            settings.method_enter_list.append(
                                method_name.replace(target_method, ''))
                        elif method_name.startswith('exit'):
                            settings.method_exit_list.append(
                                method_name.replace(target_method, ''))
                        elif method_name.startswith('visit'):
                            settings.method_visit_list.append(
                                method_name.replace(target_method, ''))

    # Enter a parse tree produced by JavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx):
        """[this method is used to process all the class declarations in the repository]

        Arguments:
            ctx {[object]} -- [overriding method gives the object of the parse tree node i.e., JavaParser.ClassDeclarationContext]
        """
        class_name = ctx.IDENTIFIER().getText()

        if ctx.typeType() is not None:
            extended_class_name = ctx.typeType().getText()

            # _considering only the child classes which are inheriting either a Base visitor or listener
            if 'BaseListener' in extended_class_name or 'BaseVisitor' in extended_class_name:
                settings.extended_class_list.append(extended_class_name)
