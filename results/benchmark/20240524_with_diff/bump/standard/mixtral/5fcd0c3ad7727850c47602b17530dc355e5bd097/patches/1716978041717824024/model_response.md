Here's a potential patch for the code, using the new `getClassInfo` method added in `ClassInfoVisitor`:

```java
import org.pitest.classinfo.ClassInfo;
import org.pitest.classinfo.ClassInfoBuilder;
import org.pitest.classinfo.ClassName;
import org.pitest.coverage.CoverageDatabase;
import org.pitest.mutationtest.ClassMutationResults;
import java.util.Set;

private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverage(className), coverage.getTimeStamp());
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This code creates a `ClassInfo` object by calling the new `getClassInfo` method, which takes a `ClassName`, a byte array containing raw coverage data, and a timestamp. The `getRawCoverage` method is used to get the raw coverage data for the mutated class.

Note that this code assumes that the `CoverageDatabase` implementation used in the original code has a `getRawCoverage` method that returns a byte array containing raw coverage data for a given class. If this assumption is incorrect, additional changes may be necessary to obtain the raw coverage data.