from JavaParserListener import JavaParserListener
from antlr4 import *
import settings


class PatternListener(JavaParserListener):

    # Enter a parse tree produced by JavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx):
        method_name = ctx.IDENTIFIER().getText()
        if method_name not in ['enterRule', 'exitRule', 'visitRule']:
            method_def_len = len(ctx.methodBody().getText()) - 2
            method_overriden_flag = ''
            if ctx.OVERRIDEN() is not None:
                method_overriden_flag = ctx.OVERRIDEN().getText()


            if method_def_len > 0 and method_overriden_flag == '@Override':
                for target_method in settings.target_method_list:
                    if method_name.startswith(target_method) and len(method_name) > len(target_method):
                        settings.method_list.append(method_name)

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
        class_name = ctx.IDENTIFIER().getText()
        
        if ctx.typeType() is not None:
            extended_class_name = ctx.typeType().getText()

            if 'BaseListener' in extended_class_name or 'BaseVisitor' in extended_class_name:
                settings.extended_class_list.append(extended_class_name)