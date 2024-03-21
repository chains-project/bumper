Here's a proposed patch to fix the failing client code:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    // Create a new ClassInfoBuilder with the mutated class name
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass().getName());
    // Get the ClassInfo object using the ClassInfoBuilder
    org.pitest.classinfo.ClassInfo classInfo = classInfoBuilder.build();
    // Create a new CoverageData object with the ClassInfo object
    org.pitest.coverage.CoverageData coverageData = new org.pitest.coverage.CoverageData(classInfo);
    // Get the ClassInfo object from the CoverageData object
    org.pitest.classinfo.ClassInfo classInfoFromCoverage = coverageData.getClassInfo();
    // Create a new MutationTestSummaryData object using the ClassInfo object
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoFromCoverage);
}
```
The patch creates a new `ClassInfoBuilder` object with the mutated class name, then uses it to build a `ClassInfo` object. The `ClassInfo` object is then used to create a new `CoverageData` object. Finally, the `ClassInfo` object is retrieved from the `CoverageData` object and used to create a new `MutationTestSummaryData` object.


The patch uses the `org.pitest.classinfo.ClassInfoBuilder` class, which is a new addition in the updated library version, to create a `ClassInfo` object without relying on the removed `getClassInfo` method.