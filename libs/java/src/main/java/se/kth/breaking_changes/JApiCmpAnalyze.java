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
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
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
                    // if(jApiClass1.getChangeStatus().equals(JApiChangeStatus.REMOVED) || jApiClass1.getChangeStatus().equals(JApiChangeStatus.NEW)) {
                    //     libraryChanges.add(new ApiChange(
                    //                 jApiClass1.getOldClass().isPresent() ? jApiClass1.getOldClass().get().getName() : "null",
                    //                 jApiClass1.getNewClass().isPresent() ? jApiClass1.getNewClass().get().getName() : "null",
                    //                 jApiClass1.getCompatibilityChanges().toString(),
                    //                 "class",
                    //                 new ApiMetadata(newJar.toFile().getName(), newJar.getFileName().getFileName()),
                    //                 new ApiMetadata(oldJar.toFile().getName(), oldJar.getFileName().getFileName())
                    //         ));
                    // }

                    //get methods
                    jApiClass1.getMethods().forEach(jApiMethod -> {
                        if (jApiMethod.getChangeStatus().equals(JApiChangeStatus.REMOVED) || jApiMethod.getChangeStatus().equals(JApiChangeStatus.NEW)) {
                            libraryChanges.add(new ApiChange(
                                    jApiMethod.getOldMethod().isPresent() ? jApiMethod.getOldMethod().get().getLongName() : "null",
                                    jApiMethod.getNewMethod().isPresent() ? jApiMethod.getNewMethod().get().getLongName() : "null",
                                    jApiMethod.getCompatibilityChanges().toString(),
                                    jApiMethod.getName(),
                                    new ApiMetadata(newJar.toFile().getName(), newJar.getFileName().getFileName()),
                                    new ApiMetadata(oldJar.toFile().getName(), oldJar.getFileName().getFileName())
                            ));
                        }
                    });
                });
            });
        });

        return libraryChanges;
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
