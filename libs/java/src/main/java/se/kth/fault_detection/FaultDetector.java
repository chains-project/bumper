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
import spoon.reflect.declaration.CtMethod;
import spoon.reflect.declaration.CtType;
import spoon.reflect.path.CtPath;
import spoon.reflect.path.CtPathBuilder;
import spoon.reflect.visitor.filter.TypeFilter;
import spoon.support.reflect.code.CtInvocationImpl;
import spoon.support.reflect.declaration.CtMethodImpl;

public class FaultDetector {
    private String dependencyGroupID;

    private Set<MavenErrorLog.ErrorInfo> mavenErrorLog;

    public FaultDetector(String dependencyGroupID, Set<MavenErrorLog.ErrorInfo> mavenErrorLog) {
        this.dependencyGroupID = dependencyGroupID;
        this.mavenErrorLog = mavenErrorLog;
    }

    public List<DetectedFault> detectFaults(String projectFilePath) {
        Launcher spoon = new Launcher();
        spoon.addInputResource(projectFilePath);
        spoon.buildModel();

        return getElementFromSourcePosition(spoon.getModel(), dependencyGroupID);
    }


    public List<DetectedFault> getElementFromSourcePosition(CtModel model, String depGrpId) {
        CtType<?> clazz = model.getAllTypes().iterator().next();
        List<DetectedFault> results = new ArrayList<>();

        for (CtMethodImpl<?> e : clazz.getElements(new TypeFilter<>(CtMethodImpl.class))) {
            if(containsAnError(e)) {
                // System.out.println("#### HERE ####");
                // System.out.println(e.getSimpleName());
                // System.out.println(getMavenErrorLog(e).getClientFilePath());
                // System.out.println(getMavenErrorLog(e).getClientLinePosition());
                // System.out.println(getMavenErrorLog(e).getErrorMessage());
                // System.out.println(e.getOriginalSourceFragment().getSourceCode());

                String dependencyIdentifier = e.getElements(new TypeFilter<>(CtInvocationImpl.class))
                    .stream()
                    .flatMap((el) -> {
                        CtPath path = new CtPathBuilder()
                                            .recursiveWildcard()
                                            .name(depGrpId)
                                            .build();
                                            
                        return path.evaluateOn(el).stream().map(line -> line.getParent().toString());
                    })
                    .filter(r -> r != null && r.contains(dependencyGroupID))
                    .findFirst()
                    .orElse("");
            
                // System.out.println("#### HERE ####");

                DetectedFault fault = new DetectedFault();
                fault.methodName = e.getSimpleName();
                // fault.methodCode = e.toString();
                fault.methodCode = e.getOriginalSourceFragment().getSourceCode();

                CtClass<?> parentClass = e.getParent(CtClass.class);
                Set<CtMethod<?>> newMethods = new HashSet<CtMethod<?>>();
                Set<CtMethod<?>> oldMethods = parentClass.getMethods();
                newMethods.add(e);
                parentClass.setMethods(newMethods);

                fault.inClassCode = parentClass.getOriginalSourceFragment().getSourceCode();

                parentClass.setMethods(oldMethods);
                

                // System.out.println(e.getOriginalSourceFragment().getSourceCode());
                // System.out.println(e.toString());

                // Need to do this trick as getLine does not take into account for decorators
                String[] lines = e.getOriginalSourceFragment().getSourceCode().split("\r\n|\r|\n");
                int numberOfLines = lines.length;
                fault.clientLineNumber = e.getPosition().getEndLine() - numberOfLines + 1; 

                fault.clientEndLineNumber = e.getPosition().getEndLine();
                fault.errorInfo = getMavenErrorLog(e);
                fault.plausibleDependencyIdentifier = dependencyIdentifier;
                results.add(fault);
            }
        }
        return results;
    }

    private MavenErrorLog.ErrorInfo getMavenErrorLog(CtElement element) {
        int startLineNumber = element.getPosition().getLine();
        int endLineNumber = element.getPosition().getEndLine();

        return mavenErrorLog
                    .stream()
                    .filter(mavenErrorLog -> {
                        int errorLineNumber = Integer.parseInt(mavenErrorLog.getClientLinePosition());
                        return errorLineNumber >= startLineNumber && errorLineNumber <= endLineNumber;
                    })
                    .findFirst()
                    .orElse(null);
    }

    private boolean containsAnError(CtElement element) {
        int startLineNumber = element.getPosition().getLine();
        int endLineNumber = element.getPosition().getEndLine();

        return mavenErrorLog.stream().anyMatch(mavenErrorLog -> {
            int errorLineNumber = Integer.parseInt(mavenErrorLog.getClientLinePosition());
            return errorLineNumber >= startLineNumber && errorLineNumber <= endLineNumber;
        });
    }
}
