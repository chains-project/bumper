package se.kth.fault_detection;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import se.kth.log_Analyzer.MavenErrorLog;
import spoon.Launcher;
import spoon.reflect.CtModel;
import spoon.reflect.declaration.CtClass;
import spoon.reflect.declaration.CtElement;
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
                // System.out.println(e.getElements(new TypeFilter<>(CtInvocationImpl.class)));
                    e.getElements(new TypeFilter<>(CtInvocationImpl.class))
                        .stream()
                        .forEach((el) -> {
                            CtPath path = new CtPathBuilder()
                                                .recursiveWildcard()
                                                .name(depGrpId)
                                                .build();
                                                
                            List<String> l = path.evaluateOn(el).stream().map(line -> line.getParent().toString()).toList();

                            // System.out.println(el.toString() + " | ");
                            // System.out.println(l);
                            // System.out.println(getDependencyMethodName(el, dependencyGroupID));
                            
                            // System.out.println(el.getTarget().getParent(CtClassImpl.class).getSuperclass());
                        });
                // System.out.println("#### HERE ####");

                DetectedFault fault = new DetectedFault();
                fault.methodName = e.getSimpleName();
                fault.methodCode = e.toString();
                fault.clientLineNumber = e.getPosition().getLine();
                fault.clientEndLineNumber = e.getPosition().getEndLine();
                fault.errorInfo = getMavenErrorLog(e);
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

    private String getDependencyMethodName(CtElement e, String dependencyGrpID) {
        CtElement parent = e.getParent(new TypeFilter<>(CtClass.class));
        while (parent != null) {
            if (String.valueOf(parent).contains(dependencyGrpID)) {
                int openingParenthesisIndex = String.valueOf(e).indexOf('(');
                if (openingParenthesisIndex != -1) {
                    return String.valueOf(e).substring(0, openingParenthesisIndex);
                }
                return String.valueOf(e);
            }
            parent = parent.getParent(new TypeFilter<>(CtClass.class));
        }
        return null;
    }
}
