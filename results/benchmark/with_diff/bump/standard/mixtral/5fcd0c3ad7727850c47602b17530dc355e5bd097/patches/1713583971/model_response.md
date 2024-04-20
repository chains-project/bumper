Here is a possible patch for the failing client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverage(className), coverage.getTimestamp());
}
```
Explanation:
The `getClassInfo` method of `CoverageDatabase` has been removed in the new library version. Instead, we can use the new `getClassInfo` method of `ClassInfoVisitor` to get the `ClassInfo` object for a given class name and coverage data.
To do this, we first extract the raw coverage data from the `CoverageDatabase` using the `getRawCoverage` method. We also need the timestamp of the coverage data, which we can get from the `CoverageDatabase` using the `getTimestamp` method.
We then pass the class name, raw coverage data, and timestamp to the `getClassInfo` method of `ClassInfoVisitor` to get the `ClassInfo` object.
We then use this `ClassInfo` object in the `createSummaryData` method instead of the one returned by the `getClassInfo` method of `CoverageDatabase`.
Note that we need to import the following classes:
```java
import org.pitest.classinfo.ClassInfo;
import org.pitest.classinfo.ClassInfoVisitor;
import org.pitest.classinfo.ClassName;
```