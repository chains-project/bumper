package se.kth.breaking_changes;

import japicmp.cli.JApiCli;
import japicmp.cmp.JApiCmpArchive;
import japicmp.cmp.JarArchiveComparator;
import japicmp.cmp.JarArchiveComparatorOptions;
import japicmp.config.Options;
import japicmp.model.AccessModifier;
import japicmp.model.JApiChangeStatus;
import japicmp.model.JApiClass;
import japicmp.output.OutputFilter;
import japicmp.util.Optional;
import javassist.NotFoundException;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.lang.reflect.Modifier;
import java.nio.file.Path;
import java.util.*;

public class JApiCmpAnalyze {
    private final Path oldJar;
    private final Path newJar;

    public JApiCmpAnalyze(Path oldJar, Path newJar) {
        this.oldJar = oldJar;
        this.newJar = newJar;
    }

    public Set<ApiChange> getChanges() {
        Options defaultOptions = getDefaultOptions();
        JarArchiveComparatorOptions comparatorOptions = JarArchiveComparatorOptions.of(defaultOptions);

        JarArchiveComparator jarArchiveComparator = new JarArchiveComparator(comparatorOptions);
        JApiCmpArchive newF = new JApiCmpArchive(newJar.toFile(), newJar.getFileName().toString());
        JApiCmpArchive old = new JApiCmpArchive(oldJar.toFile(), oldJar.getFileName().toString());

        List<JApiClass> jApiClasses = jarArchiveComparator.compare(old, newF);
        OutputFilter filter = new OutputFilter(defaultOptions);
        filter.filter(jApiClasses);
        Set<ApiChange> libraryChanges = new HashSet<>();

        //list of classes
        jApiClasses.forEach(jApiClass -> {
            //read incompatible changes
            jApiClass.getCompatibilityChanges().forEach(jApiCompatibilityChange -> {

                //go for each change
                jApiClasses.iterator().forEachRemaining(jApiClass1 -> {
                    jApiClass1.getConstructors().forEach(jApiConstructor -> {
                        if (jApiConstructor.getChangeStatus().equals(JApiChangeStatus.NEW)) {
                            libraryChanges.add(
                                new ApiChange()
                                    .setAction(ApiChangeType.ADD)
                                    .setModifier(jApiConstructor.getNewConstructor().get().getModifiers())
                                    .setReturnType(jApiConstructor.getName())
                                    .setElement(jApiConstructor.getNewConstructor().get().getLongName())
                                    .setCategory(jApiConstructor.getCompatibilityChanges().toString())
                                    .setName(jApiConstructor.getName())
                                    .setNewVersion(new ApiMetadata(newJar.toFile().getName(), newJar.getFileName().getFileName()))
                                    .setOldVersion(new ApiMetadata(oldJar.toFile().getName(), oldJar.getFileName().getFileName()))
                            );
                        } else if (jApiConstructor.getChangeStatus().equals(JApiChangeStatus.REMOVED)) {
                            libraryChanges.add(
                                new ApiChange()
                                    .setAction(ApiChangeType.REMOVE)
                                    .setModifier(jApiConstructor.getOldConstructor().get().getModifiers())
                                    .setReturnType(jApiConstructor.getName())
                                    .setElement(jApiConstructor.getOldConstructor().get().getLongName())
                                    .setCategory(jApiConstructor.getCompatibilityChanges().toString())
                                    .setName(jApiConstructor.getName())
                                    .setNewVersion(new ApiMetadata(newJar.toFile().getName(), newJar.getFileName().getFileName()))
                                    .setOldVersion(new ApiMetadata(oldJar.toFile().getName(), oldJar.getFileName().getFileName()))
                            );
                        }
                    });

                    //get methods
                    jApiClass1.getMethods().forEach(jApiMethod -> {
                        if (jApiMethod.getChangeStatus().equals(JApiChangeStatus.NEW)) {
                            libraryChanges.add(
                                new ApiChange()
                                    .setAction(ApiChangeType.ADD)
                                    .setModifier(jApiMethod.getNewMethod().get().getModifiers())
                                    .setReturnType(this.getReturnType(jApiMethod.getNewMethod().get().getSignature()))
                                    .setElement(jApiMethod.getNewMethod().get().getLongName())
                                    .setCategory(jApiMethod.getCompatibilityChanges().toString())
                                    .setName(jApiMethod.getName())
                                    .setNewVersion(new ApiMetadata(newJar.toFile().getName(), newJar.getFileName().getFileName()))
                                    .setOldVersion(new ApiMetadata(oldJar.toFile().getName(), oldJar.getFileName().getFileName()))
                            );
                        } else if (jApiMethod.getChangeStatus().equals(JApiChangeStatus.REMOVED)) {
                            libraryChanges.add(
                                new ApiChange()
                                    .setAction(ApiChangeType.REMOVE)
                                    .setModifier(jApiMethod.getOldMethod().get().getModifiers())
                                    .setReturnType(this.getReturnType(jApiMethod.getOldMethod().get().getSignature()))
                                    .setElement(jApiMethod.getOldMethod().get().getLongName())
                                    .setCategory(jApiMethod.getCompatibilityChanges().toString())
                                    .setName(jApiMethod.getName())
                                    .setNewVersion(new ApiMetadata(newJar.toFile().getName(), newJar.getFileName().getFileName()))
                                    .setOldVersion(new ApiMetadata(oldJar.toFile().getName(), oldJar.getFileName().getFileName()))
                            );
                        } else if (jApiMethod.getChangeStatus().equals(JApiChangeStatus.MODIFIED)) {
                            System.out.println("MODIFIED: " + jApiMethod.getOldMethod().get().getLongName());
                            libraryChanges.add(
                                new ApiChange()
                                    .setAction(ApiChangeType.REMOVE)
                                    .setModifier(jApiMethod.getOldMethod().get().getModifiers())
                                    .setReturnType(this.getReturnType(jApiMethod.getOldMethod().get().getSignature()))
                                    .setElement(jApiMethod.getOldMethod().get().getLongName())
                                    .setCategory(jApiMethod.getCompatibilityChanges().toString())
                                    .setName(jApiMethod.getName())
                                    .setNewVersion(new ApiMetadata(newJar.toFile().getName(), newJar.getFileName().getFileName()))
                                    .setOldVersion(new ApiMetadata(oldJar.toFile().getName(), oldJar.getFileName().getFileName()))
                            );
                            libraryChanges.add(
                                new ApiChange()
                                    .setAction(ApiChangeType.ADD)
                                    .setModifier(jApiMethod.getNewMethod().get().getModifiers())
                                    .setReturnType(this.getReturnType(jApiMethod.getNewMethod().get().getSignature()))
                                    .setElement(jApiMethod.getNewMethod().get().getLongName())
                                    .setCategory(jApiMethod.getCompatibilityChanges().toString())
                                    .setName(jApiMethod.getName())
                                    .setNewVersion(new ApiMetadata(newJar.toFile().getName(), newJar.getFileName().getFileName()))
                                    .setOldVersion(new ApiMetadata(oldJar.toFile().getName(), oldJar.getFileName().getFileName()))
                            );
                        }
                    });
                });
            });
        });

        return libraryChanges;
    }

    private String getReturnType(String fromSignature) {
        int semicolonIndex = fromSignature.indexOf(')');
        String type = fromSignature.substring(semicolonIndex + 1);

        if(type.equals("Z")) {
            return "bool";
        } else if (type.equals("V")) {
            return "void";
        } else if (type.equals("I")) {
            return "int";
        } else if (type.indexOf("L") < 0) {
            return type;
        }

        
        type = type
            .replace("/", ".")
            .replace(";", "");

        // for generics
        type = type.replace("[", "");

        // Remove the initial L that indicates that return type is a class
        type = type.substring(1);

        return type;
    }

    private static Options getDefaultOptions() {
        Options defaultOptions = Options.newDefault();
        defaultOptions.setAccessModifier(AccessModifier.PROTECTED);
        defaultOptions.setOutputOnlyModifications(true);
        defaultOptions.setXmlOutputFile(Optional.of("output.xml"));
        defaultOptions.setClassPathMode(JApiCli.ClassPathMode.TWO_SEPARATE_CLASSPATHS);
        defaultOptions.setIgnoreMissingClasses(true);
        defaultOptions.setReportOnlyFilename(true);
        String[] excl = {"(*.)?tests(.*)?", "(*.)?test(.*)?",
                "@org.junit.After", "@org.junit.AfterClass",
                "@org.junit.Before", "@org.junit.BeforeClass",
                "@org.junit.Ignore", "@org.junit.Test",
                "@org.junit.runner.RunWith"};

        for (String e : excl) {
            defaultOptions.addExcludeFromArgument(Optional.of(e), false);
        }

        return defaultOptions;
    }

}
