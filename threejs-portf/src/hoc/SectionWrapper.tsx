import { motion } from 'framer-motion';

import { styles } from '../style';
import { staggerContainer } from '../utils/motion';

const SectionWrapper = (Component, idName) => function HOC() {
    return (
        <motion.section
            variants={staggerContainer()}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.25 }}
            className=""
        >
        <Component />
        </motion.section>
    )
}

export default SectionWrapper
