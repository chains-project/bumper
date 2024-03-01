package se.kth.fault_detection;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import se.kth.log_Analyzer.MavenErrorLog;
import spoon.Launcher;
import spoon.reflect.CtModel;
import spoon.reflect.declaration.CtClass;
import spoon.reflect.declaration.CtElement;
import spoon.reflect.declaration.CtImport;
import spoon.reflect.declaration.CtMethod;
import spoon.reflect.declaration.CtType;
import spoon.reflect.visitor.filter.TypeFilter;
import spoon.support.reflect.declaration.CtMethodImpl;

public class FaultDetector {
    private Set<MavenErrorLog.ErrorInfo> mavenErrorLog;

    public FaultDetector(Set<MavenErrorLog.ErrorInfo> mavenErrorLog) {
        this.mavenErrorLog = mavenErrorLog;
    }

    public List<DetectedFault> detectFaults(String projectFilePath) {
        Launcher spoon = new Launcher();
        spoon.getEnvironment().setAutoImports(true);
        spoon.addInputResource(projectFilePath);
        spoon.buildModel();

        CtModel model = spoon.getModel();
        List<DetectedFault> result = new ArrayList<DetectedFault>();

        // Order is very important as you tipically want to fix from the first error
        result.addAll(getImportFaults(model));
        result.addAll(getMethodFaults(model));

        return result;
    }

    private MavenErrorLog.ErrorInfo getMavenErrorLog(CtElement element) {
        int startLineNumber = this.getRealLinePosition(element);
        int endLineNumber = element.getPosition().getEndLine();

        return mavenErrorLog
                    .stream()
                    .filter(mavenErrorLog -> {
                        int errorLineNumber = Integer.parseInt(mavenErrorLog.getClientLinePosition());
                        element.toString();
                        return errorLineNumber >= startLineNumber && errorLineNumber <= endLineNumber;
                    })
                    .findFirst()
                    .orElse(null);
    }

    private boolean containsAnError(CtElement element) {
        int startLineNumber = this.getRealLinePosition(element);
        int endLineNumber = element.getPosition().getEndLine();

        return mavenErrorLog.stream().anyMatch(mavenErrorLog -> {
            int errorLineNumber = Integer.parseInt(mavenErrorLog.getClientLinePosition());
            return errorLineNumber >= startLineNumber && errorLineNumber <= endLineNumber;
        });
    }

    private int getRealLinePosition(CtElement element) {
        // Need to do this trick as getLine does not take into account for decorators, and comments
        String[] lines = element.getOriginalSourceFragment().getSourceCode().split("\r\n|\r|\n");
        int numberOfLines = lines.length;
        return element.getPosition().getEndLine() - numberOfLines + 1;
    }

    private List<DetectedFault> getImportFaults(CtModel model) {
        CtType<?> mainClass = model.getAllTypes().iterator().next();
        List<DetectedFault> result = new ArrayList<DetectedFault>();

        mainClass.getPosition().getCompilationUnit().getImports().stream()
            .forEach((CtElement element) -> {
                if(this.containsAnError(element)) {
                    result.add(
                        new DetectedFault()
                            .setMethodName("import")
                            .setMethodCode(element.toString())
                            .setClientLineNumber(element.getPosition().getLine())
                            .setClientEndLineNumber(element.getPosition().getEndLine())
                            .setErrorInfo(getMavenErrorLog(element))
                    );
                }
            });

        return result;
    }

    private List<DetectedFault> getMethodFaults(CtModel model) {
        CtType<?> mainClass = model.getAllTypes().iterator().next();
        List<DetectedFault> results = new ArrayList<>();

        mainClass.getElements(new TypeFilter<>(CtMethodImpl.class)).stream().forEach(e -> {
            if(this.containsAnError(e)) {
                DetectedFault fault = new DetectedFault();
                fault.methodName = e.getSimpleName();
                fault.qualifiedMethodCode = e.toStringDebug();
                fault.methodCode = e.getOriginalSourceFragment().getSourceCode();

                CtClass<?> parentClass = e.getParent(CtClass.class);
                Set<CtMethod<?>> newMethods = new HashSet<CtMethod<?>>();
                Set<CtMethod<?>> oldMethods = parentClass.getMethods();
                newMethods.add(e);
                
                parentClass.setMethods(newMethods);

                fault.inClassCode = parentClass.toString();
                fault.qualifiedInClassCode = parentClass.toStringDebug();
                parentClass.setMethods(oldMethods);
                
                fault.clientLineNumber = getRealLinePosition(e);
                fault.clientEndLineNumber = e.getPosition().getEndLine();
                fault.errorInfo = getMavenErrorLog(e);
                fault.plausibleDependencyIdentifier = null;
                results.add(fault);
            }
        });
        return results;
    }
}
