import React from 'react'
import { motion } from 'framer-motion';
import { styles } from '../style';
import { ComputersCanvas } from './canvas';

// 40:00

const Hero = () => {
  return (
    <section className='realative w-full h-screen mx-auto'>
      <div className={`${styles.paddingX} absolute inset-0 top-[120px] max-w-7xl mx-auto flex flex-row items-start gap-5`}>
        <div className='flex flex-col justify-center items-center mt-5'>
          <div className='w-3 h-3 rounded-full bg-[#33cce0]' />
            <div className='w-1 sm:h-80 h-60 bg-gradient-to-t from-blue-600 to-[#33cce0]' />
                    <div className='w-2 h-2 rounded-full bg-blue-600' />
         </div>
      <div>
        <h1 className={`${styles.heroHeadText} text-white`}>Magnus <span className='text-[#33cce0]'>Fröbom</span></h1>
        <p className={`${styles.heroSubText} mt-2 text-white`}>
         Creative Tech Entusiast, I code, Dream<br className='sm:block hidden' /> I love learning new stuff.
        </p>
      </div>
      </div>
      
        <ComputersCanvas />
        <div className='absolute xs:bottom-10 bottom-32 w-full flex justify-center items-center'>
          <a href='#about'>
            <div className='w-[35px] h-[64px] rounded-3xl border-4 border-secondary flex justify-center items-start p-2'>
              <motion.div 
                animate={{
                  y: [0, 24, 0]
                }}
                transition={{
                  duration: 1.5,
                  repeat: Infinity,
                  repeatType: 'loop'
                }}
                className="w-3 h-3 rounded-full bg-secondary mb-1 "
              />

            </div>
          </a>
        </div>
    </section>
  )
}

export default Hero