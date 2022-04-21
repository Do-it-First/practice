import { FunctionComponent } from "react";
import styles from "./css/Desktop1.module.css";

export const Desktop1: FunctionComponent = () => {
  return (
    <div className={styles.desktop1}>
      <div className={styles.frameDiv}>
        <div className={styles.div}>
          <p className={styles.p}>일단해보조</p>
          <p className={styles.p1}>웹툰 통합플랫폼</p>
        </div>
        <div className={styles.div1}>
          <div className={styles.rectangleDiv} />
          <div className={styles.div2}>검색단어</div>
        </div>
      </div>
    </div>
  );
};
